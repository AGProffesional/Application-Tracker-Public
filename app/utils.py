def Wordify_application(app_obj):
    return {
        "application_id": app_obj.application_id,
        "user_id": app_obj.user_id,
        "company_name": app_obj.company_name,
        "position_name": app_obj.position_name,
        "application_status": app_obj.application_status,
        "application_date": app_obj.application_date,
        "application_deadline": app_obj.application_deadline,
        "followed_up_status": "Yes" if app_obj.followed_up_status else "No",
        "interviewed_status": "Yes" if app_obj.interviewed_status else "No",
        "resume_link": app_obj.resume_link,
        "notes": app_obj.notes,
    }
