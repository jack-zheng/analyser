import os
import requests
from dotenv import load_dotenv
import logging

from flask import Blueprint, render_template, flash, redirect, url_for

from app.forms import RegisterProvisioner, MapCompany


provisioner_bp = Blueprint('provisioner', __name__)
load_dotenv()
domianurl = os.getenv('domainurl')
basic_token = os.getenv('rest_basic_token')


def get_access_token():
    # get rest API token
    payload = '{"grant_type":"client_credentials",\
        "scope":"userId=SFV4,resourceType=sfprovisioning"}'
    url = "%s/api/oauth/rest/v1/token" % domianurl
    headers = {
        'Content-type': "application/json",
        'Authorization': basic_token}

    response = requests.request("POST", url, data=payload, headers=headers)
    logging.warning("Get token status: %s" % response.status_code)

    json_ret = response.json()
    return "%s %s" % (json_ret['token_type'], json_ret['access_token'])


@provisioner_bp.route('/register', methods=['GET', 'POST'])
def register_provisioner():
    form = RegisterProvisioner()
    if form.validate_on_submit():
        inumber = form.inumber.data
        email = form.email.data

        # send request to create provisioner
        prov_header = {
            'Content-type': "application/json",
            'Authorization': get_access_token()
        }

        prov_payload = '{"provisionerId": "%s",\
            "provisionerName":"%s","provisionerPassword":"pwd",\
                "provisionerEmail":"%s"}' % (inumber, inumber, email)

        prov_url = "%s/provisioningapi/provisioning/dataservice"\
            "/rest/v1/createprovisioner" % domianurl

        resp = requests.request(
            "POST", prov_url, data=prov_payload, headers=prov_header)
        logging.warning("Create provisioner status: %s" % resp.status_code)

        # permission flag: 16777218, edit company + disable popup
        permission_payload = '{"provisionerId":"%s",\
            "provisionerFlag":"16777234"}' % inumber
        permission_url = "%s/provisioningapi/provisioning/dataservice"\
            "/rest/v1/setprovisionerperm" % domianurl
        resp = requests.request(
            "POST", permission_url, data=permission_payload,
            headers=prov_header)
        logging.warning("Assign permission status: %s" % resp.status_code)

        flash('Provisioner account has been created. \
            please clean browser cache and re-login.', 'success')
        return redirect(url_for('.map_company', inumber=inumber))
    return render_template('provisioner/register_provisioner.html', form=form)


@provisioner_bp.route(
    '/map-company', defaults={'inumber': ''}, methods=['GET', 'POST'])
@provisioner_bp.route('/map-company/<inumber>', methods=['GET', 'POST'])
def map_company(inumber):
    form = MapCompany()
    form.inumber.data = inumber
    if form.validate_on_submit():
        id = form.inumber.data
        cid = form.company.data

        # send request to map provisioner to company
        headers = {
            'Content-type': "application/json",
            'Authorization': get_access_token()
        }
        url = "%s/provisioningapi/provisioning/dataservice/"\
            "rest/v1/mapprovisionertocompany" % domianurl
        payload = '{"provisionerId" : "%s","companyId": "%s"}' % (id, cid)
        resp = requests.request("POST", url, data=payload, headers=headers)
        if resp.status_code == 200:
            flash(
                'Company: %s has mapped to provisioner: %s' % (id, cid),
                'success')
        else:
            flash('Map failed, error %s' % resp.text, 'danger')
        return redirect(url_for('.map_company'))
    return render_template('/provisioner/map_company.html', form=form)
