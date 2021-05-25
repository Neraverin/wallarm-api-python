from enum import Enum


class Role(Enum):
    ADMIN = 'admin'
    SUPER_ADMIN = 'superadmin'
    ANALYTIC = 'analytic'
    AUDITOR = 'auditor'
    DEPLOY = 'deploy'
    PARTNER_ADMIN = 'partner_admin'
    PARTNER_ANALITYC = 'partner_analytic'
    PARTNER_AUDITOR = 'partner_auditor'
    NODE = "node"
    # seems custom
    CREATE_NODE = "create_node"
    VIEW_LICENSE = "view_license"
