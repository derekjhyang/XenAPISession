#!/usr/bin/env python

import XenAPI

class Session:
    def __init__(self, url, user, pw):
        self.session = XenAPI.Session(url)
        self.xapi = self.session.xenapi
        self.xapi.login_with_password(user, pw)

def getPoolwideVMs(session):
    vm_refs = session.xapi.VM.get_all()
    vms = []
    for vm_ref in vm_refs:
        if not ( session.xapi.VM.get_record(vm_ref).get("is_a_template") and
                 session.xapi.VM.get_record(vm_ref).get("is_control_domain") ):
            vms.append(vm_ref)
    return vms

def getPoolwideHosts(session):
    return session.xapi.host.get_all()


def get_allAvailHostingVMOpaqueRef(session):
    host_opaque_ref = session.xapi.host.get_by_name_label(self.hostname)[0]
    if host_opaque_ref == "":
        return []
    else:
        return session.xapi.host.get_record(host_opaque_ref).get('resident_VMs')
