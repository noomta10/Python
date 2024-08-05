# JIRA_PLUGINS = {
#     "administer": "https://marketplace.atlassian.com/apps/1221078/custom-fields-administrator-for-jira-project?hosting=datacenter&tab=overview",
#     "capacity": "https://marketplace.atlassian.com/apps/1218151/capacity-tracker?hosting=datacenter&tab=overview",
#     "dashboard": "https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-tables?hosting=datacenter&tab=overview",
#     "project": "https://marketplace.atlassian.com/apps/1211147/project-configurator-for-jira?hosting=datacenter&tab=overview",
#     "time": "https://marketplace.atlassian.com/apps/1219732/time-in-status?hosting=datacenter&tab=overview"
# }

# CONFLUENCE_PLUGINS = {
#     "azure": "https://marketplace.atlassian.com/apps/1223149/azure-devops-confluence-connector?hosting=datacenter&tab=overview",
#     "cenote": "https://marketplace.atlassian.com/apps/36199/cenote-lockpoint-attachment-check-out?hosting=datacenter&tab=overview",
#     "content": "https://marketplace.atlassian.com/apps/247/content-formatting-macros-for-confluence?hosting=datacenter&tab=overview",
#     "page": "https://marketplace.atlassian.com/apps/1217079/page-view-tracker?hosting=datacenter&tab=overview",
#     "rtl": "https://marketplace.atlassian.com/apps/1228597/rtl-for-confluence?hosting=datacenter&tab=overview"
# }

JIRA_PLUGINS = {"project": "https://marketplace.atlassian.com/apps/1211147/project-configurator-for-jira?hosting=datacenter&tab=overview"}
CONFLUENCE_PLUGINS = {"page": "https://marketplace.atlassian.com/apps/1217079/page-view-tracker?hosting=datacenter&tab=overview"}
ATLASSIAN_PLUGINS = JIRA_PLUGINS | CONFLUENCE_PLUGINS 