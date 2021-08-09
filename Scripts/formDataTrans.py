
def formDataTrans(requiredDataObj):
    '''
    keyList1 = ['_VAR_EXECUTE_INDEP_ORGANIZE_Name', '_VAR_ACTION_INDEP_ORGANIZES_Codes', '_VAR_ACTION_REALNAME',
                '_VAR_ACTION_ORGANIZE', '_VAR_EXECUTE_ORGANIZE', '_VAR_ACTION_INDEP_ORGANIZE',
                '_VAR_ACTION_INDEP_ORGANIZE_Name', '_VAR_ACTION_ORGANIZE_Name', '_VAR_EXECUTE_ORGANIZES_Names',
                '_VAR_OWNER_ORGANIZES_Codes', '_VAR_ADDR', '_VAR_OWNER_ORGANIZES_Names', '_VAR_URL',
                '_VAR_EXECUTE_ORGANIZE_Name', '_VAR_RELEASE', '_VAR_TODAY', '_VAR_NOW_MONTH', '_VAR_ACTION_USERCODES',
                '_VAR_ACTION_EMAIL', '_VAR_ACTION_ACCOUNT', '_VAR_ACTION_INDEP_ORGANIZES_Names', '_VAR_OWNER_ACCOUNT',
                '_VAR_ACTION_ORGANIZES_Names', '_VAR_STEP_CODE', '_VAR_OWNER_USERCODES', '_VAR_EXECUTE_ORGANIZES_Codes',
                '_VAR_NOW_DAY', '_VAR_OWNER_EMAIL', '_VAR_OWNER_REALNAME', '_VAR_NOW', '_VAR_URL_Attr',
                '_VAR_ENTRY_NUMBER', '_VAR_EXECUTE_INDEP_ORGANIZES_Names', '_VAR_STEP_NUMBER', '_VAR_POSITIONS',
                '_VAR_EXECUTE_INDEP_ORGANIZES_Codes', '_VAR_EXECUTE_POSITIONS', '_VAR_ACTION_ORGANIZES_Codes',
                '_VAR_EXECUTE_INDEP_ORGANIZE', '_VAR_NOW_YEAR', 'fieldFLid', 'fieldSQSJ', 'fieldJBXXxm',
                'fieldJBXXxm_Name', 'fieldJBXXgh', 'fieldJBXXxb', 'fieldJBXXxb_Name', 'fieldJBXXlxfs', 'fieldJBXXdw',
                'fieldJBXXdw_Name', 'fieldJBXXnj', 'fieldJBXXsfzh', 'fieldJBXXJG', 'fieldJBXXfdyxm',
                'fieldJBXXfdyxm_Name', 'fieldJBXXfdygh', 'fieldJBXXjgs', 'fieldJBXXjgs_Name', 'fieldJBXXjgshi',
                'fieldJBXXjgshi_Name', 'fieldJBXXjgq', 'fieldJBXXjgq_Name', 'fieldJBXXjgsjtdz', 'fieldJBXXjjlxr',
                'fieldJBXXjjlxrdh', 'fieldSTQKsfstbs', 'fieldSTQKks', 'fieldSTQKgm', 'fieldSTQKfs', 'fieldSTQKfl',
                'fieldSTQKhxkn', 'fieldSTQKfx', 'fieldSTQKqt', 'fieldSTQKqtms', 'fieldSTQKfrtw', 'fieldWXTS',
                'fieldSTQKqtqksm', 'fieldSTQKdqstzk', 'fieldCXXXcxzt', 'fieldCXXXjtzz', 'fieldCXXXjtzz_Name',
                'fieldCXXXjtzzs', 'fieldCXXXjtzzs_Name', 'fieldCXXXjtzzq', 'fieldCXXXjtzzq_Name', 'fieldCXXXjtjtzz',
                'fieldCXXXfxxq', 'fieldCXXXfxxq_Name', 'fieldCXXXssh', 'fieldCXXXdqszd', 'fieldCXXXcqwdq',
                'fieldCXXXjtfsfj', 'fieldCXXXjtfshc', 'fieldCXXXjtfsdb', 'fieldCXXXjtfspc', 'fieldCXXXjtfslc',
                'fieldCXXXjtfsqt', 'fieldCXXXjtfsqtms', 'fieldCXXXjtgjbc', 'fieldYQJLjrsfczbl', 'fieldYQJLjrsfczbldqzt',
                'fieldYQJLsfjcqtbl', 'fieldCXXXsftjwh', 'fieldCXXXsftjhb', 'fieldCXXXsftjhbss', 'fieldCXXXsftjhbs',
                'fieldCXXXsftjhbs_Name', 'fieldCXXXsftjhbq', 'fieldCXXXsftjhbq_Name', 'fieldCXXXsftjhbjtdz', 'fieldYC',
                'fieldMQJCRxh', 'fieldMQJCRxm', 'fieldMQJCRlxfs', 'fieldMQJCRcjdd', 'fieldCNS']

    :param requiredDataObj:
    :return:
    '''
    keyList1 = ['_VAR_EXECUTE_INDEP_ORGANIZE_Name', '_VAR_ACTION_INDEP_ORGANIZES_Codes', '_VAR_ACTION_REALNAME',
                '_VAR_ACTION_ORGANIZE', '_VAR_EXECUTE_ORGANIZE', '_VAR_ACTION_INDEP_ORGANIZE',
                '_VAR_ACTION_INDEP_ORGANIZE_Name', '_VAR_ACTION_ORGANIZE_Name', '_VAR_EXECUTE_ORGANIZES_Names',
                '_VAR_OWNER_ORGANIZES_Codes', '_VAR_ADDR', '_VAR_OWNER_ORGANIZES_Names', '_VAR_URL',
                '_VAR_EXECUTE_ORGANIZE_Name', '_VAR_RELEASE', '_VAR_TODAY', '_VAR_NOW_MONTH', '_VAR_ACTION_USERCODES',
                '_VAR_ACTION_EMAIL', '_VAR_ACTION_ACCOUNT', '_VAR_ACTION_INDEP_ORGANIZES_Names', '_VAR_OWNER_ACCOUNT',
                '_VAR_ACTION_ORGANIZES_Names', '_VAR_STEP_CODE', '_VAR_OWNER_USERCODES', '_VAR_EXECUTE_ORGANIZES_Codes',
                '_VAR_NOW_DAY', '_VAR_OWNER_EMAIL', '_VAR_OWNER_REALNAME', '_VAR_NOW', '_VAR_URL_Attr',
                '_VAR_ENTRY_NUMBER', '_VAR_EXECUTE_INDEP_ORGANIZES_Names', '_VAR_STEP_NUMBER', '_VAR_POSITIONS',
                '_VAR_EXECUTE_INDEP_ORGANIZES_Codes', '_VAR_EXECUTE_POSITIONS', '_VAR_ACTION_ORGANIZES_Codes',
                '_VAR_EXECUTE_INDEP_ORGANIZE', '_VAR_NOW_YEAR', 'groupMQJCRList', 'fieldFLid', 'fieldSQSJ',
                'fieldJBXXxm', 'fieldJBXXxm_Name', 'fieldJBXXgh', 'fieldJBXXxb', 'fieldJBXXxb_Name', 'fieldJBXXlxfs',
                'fieldJBXXdw', 'fieldJBXXdw_Name', 'fieldJBXXnj', 'fieldJBXXsfzh', 'fieldJBXXJG', 'fieldJBXXcsny',
                'fieldJBXXfdyxm', 'fieldJBXXfdyxm_Name', 'fieldJBXXfdygh', 'fieldJBXXjgs', 'fieldJBXXjgs_Name',
                'fieldJBXXjgshi', 'fieldJBXXjgshi_Name', 'fieldJBXXjgshi_Attr', 'fieldJBXXjgq', 'fieldJBXXjgq_Name',
                'fieldJBXXjgq_Attr', 'fieldJBXXjgsjtdz', 'fieldJBXXjjlxr', 'fieldJBXXjjlxrdh', 'fieldSTQKsfstbs',
                'fieldSTQKks', 'fieldSTQKgm', 'fieldSTQKfs', 'fieldSTQKfl', 'fieldSTQKhxkn', 'fieldSTQKfx',
                'fieldSTQKqt', 'fieldSTQKqtms', 'fieldSTQKfrtw', 'fieldWXTS', 'fieldSTQKqtqksm', 'fieldSTQKdqstzk',
                'fieldSTQKglsjrq', 'fieldSTQKglsjsf', 'fieldSTQKfrsjrq', 'fieldSTQKfrsjsf', 'fieldCXXXcxzt',
                'fieldCXXXjtzz', 'fieldCXXXjtzz_Name', 'fieldCXXXjtzzs', 'fieldCXXXjtzzs_Name', 'fieldCXXXjtzzs_Attr',
                'fieldCXXXjtzzq', 'fieldCXXXjtzzq_Name', 'fieldCXXXjtzzq_Attr', 'fieldCXXXjtjtzz', 'fieldCXXXfxxq',
                'fieldCXXXfxxq_Name', 'fieldCXXXssh', 'fieldCXXXdqszd', 'fieldCXXXcqwdq', 'fieldCXXXfxcfsj',
                'fieldCXXXjtfsfj', 'fieldCXXXjtfshc', 'fieldCXXXjtfsdb', 'fieldCXXXjtfspc', 'fieldCXXXjtfslc',
                'fieldCXXXjtfsqt', 'fieldCXXXjtfsqtms', 'fieldCXXXjtgjbc', 'fieldYQJLjrsfczbl', 'fieldYQJLjrsfczbldqzt',
                'fieldYQJLsfjcqtbl', 'fieldCXXXsftjwh', 'fieldCXXXsftjhb', 'fieldCXXXsftjhbss',
                'fieldCXXXsftjhbss_Name', 'fieldCXXXsftjhbs', 'fieldCXXXsftjhbs_Name', 'fieldCXXXsftjhbs_Attr',
                'fieldCXXXsftjhbq', 'fieldCXXXsftjhbq_Name', 'fieldCXXXsftjhbq_Attr', 'fieldCXXXsftjhbjtdz', 'fieldYC',
                'fieldMQJCRxh', 'fieldMQJCRxm', 'fieldMQJCRlxfs', 'fieldMQJCRcjdd', 'fieldCNS', '_VAR_ENTRY_NAME',
                '_VAR_ENTRY_TAGS']
    formData2Obj = {}
    for key in keyList1:
        formData2Obj[key] = ''
        if key in requiredDataObj:
            formData2Obj[key] = requiredDataObj[key]
    formData2Obj["_VAR_RELEASE"] = "true"
    formData2Obj["fieldSTQKfrtw"] = "36.5"
    formData2Obj["fieldCXXXfxxq"] = "1"
    formData2Obj["fieldCXXXfxxq_Name"] = "南京校区"
    formData2Obj["fieldCNS"] = True
    formData2Obj["groupMQJCRList"] = [0]
    formData2Obj["fieldJBXXcsny"] = ""
    formData2Obj["fieldJBXXjgshi_Attr"] = "{\"_parent\":\"" + formData2Obj["fieldJBXXjgs"] + "\"}"
    # 市的父节点：省编号，这两个是籍贯
    formData2Obj["fieldJBXXjgq_Attr"] = "{\"_parent\":\"" + formData2Obj["fieldJBXXjgshi"] + "\"}"
    # 区的父节点：市编号
    formData2Obj["fieldSTQKglsjrq"] = ""
    formData2Obj["fieldSTQKglsjsf"] = ""
    formData2Obj["fieldSTQKfrsjrq"] = ""
    formData2Obj["fieldSTQKfrsjsf"] = ""
    formData2Obj["fieldCXXXjtzzs_Attr"] = "{\"_parent\":\"" + formData2Obj["fieldCXXXjtzz"] + "\"}"
    formData2Obj["fieldCXXXjtzzq_Attr"] = "{\"_parent\":\"" + formData2Obj["fieldCXXXjtzzs"] + "\"}"
    # 两个所在地的父节点
    formData2Obj["fieldCXXXfxcfsj"] = ""
    formData2Obj["fieldCXXXsftjhbss_Name"] = ""
    formData2Obj["fieldCXXXsftjhbs_Attr"] = "{\"_parent\":\"" + formData2Obj["fieldCXXXsftjhbss"] + "\"}"
    formData2Obj["fieldCXXXsftjhbq_Attr"] = "{\"_parent\":\"" + formData2Obj["fieldCXXXsftjhbq"] + "\"}"
    # 中高风险区的父节点
    formData2Obj["_VAR_ENTRY_NAME"] = "学生健康状况申报"
    formData2Obj["_VAR_ENTRY_TAGS"] = "学工部"
    return formData2Obj
