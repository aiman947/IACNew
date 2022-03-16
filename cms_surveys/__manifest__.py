# -*- coding: utf-8 -*-
{
    'name': "CMS Surveys",

    'summary': """
        FeedBack System""",

    'description': """
        Surveys form are customized to make it usable
            """,

    'author': "GlobalXS",
    'website': "http://www.globalxs.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'survey', 'odoocms', 'odoocms_academic', 'odoocms_registration', 'website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/survey_setup_view.xml',
        'views/survey_template_view.xml',
        'wizards/survey_wizards_view.xml',
        'wizards/sada_survey_wizards_view.xml',
        'wizards/survey_deadline_extend_wizards_view.xml',
        'wizards/sada_survey_class_audit_view.xml',
        'reports/report.xml',
        'reports/report_prepare_result_pdf.xml',
        # 'data/survey.types.csv',
        # 'data/survey.label.csv',
        # 'data/survey.survey.csv',
        # 'data/survey.question.csv',
        'data/cms_survey_sequence.xml',
        'data/cms_survey_cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}