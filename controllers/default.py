# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
def test_event_type():
    return locals()

def test_states():
    return locals()

def list():
    table = db(db.events.status.contains("Upcoming")).select()
    placeholder = True
    company_flag = False
    events_flag = False
    location_flag = False
    people_flag = False
    if request.vars.company_name:
        company_name = request.vars.company_name
        company_table = db.company(name=company_name)
        if request.vars.option == "location":
            location_flag = True
            placeholder = False
            id = company_table.id
            table = db(db.locations.company_id == id).select()
            print(table)
        elif request.vars.option == "contacts":
            people_flag = True
            placeholder = False
            id = company_table.id
            table = db(db.people.company_id == id).select()
    elif request.vars.person_name:
        full_name = request.vars.person_name
        name_list = full_name.split(" ")
        name = name_list[0]
        person = db.people(first_name=name)
        if request.vars.option == "all":
            events_flag = True
            placeholder = False
            id = person.id
            table = db(db.events.person_id == id).select()
            print(table)
        elif request.vars.option == "upcoming":
            events_flag = True
            placeholder = False
            id = person.id
            table = db((db.events.person_id == id) & (db.events.status.contains("Upcoming"))).select()
            print(table)
        elif request.vars.option == "completed":
            events_flag = True
            placeholder = False
            id = person.id
            table = db((db.events.person_id == id) & (db.events.status.contains("Completed"))).select()
            print(table)
    return locals()

def test_location():
    return locals()

def test_people():
    return locals()

def test_events():
    return locals()

def test_people_type():
    return locals()

def test_social_media():
    return locals()

# ---- example index page ----
def add_record():
    if request.args(0) == 'event_type':
        table = db.event_type
    elif request.args(0) == 'states':
        table = db.states
    elif request.args(0) == 'company':
        table = db.company
    elif request.args(0) == 'locations':
        table = db.locations
    elif request.args(0) == 'people':
        table = db.people
    elif request.args(0) == 'events':
        table = db.event
    elif request.args(0) == 'people_type':
        table = db.people_type
    elif request.args(0) == 'social_media':
        table = db.social_media
    form = SQLFORM(table)
    return locals()

def edit():
    id = request.args(0, cast=int)
    if request.args(1) == 'event_type':
        table = db.event_type
    elif request.args(1) == 'states':
        table = db.states
    elif request.args(1) == 'company':
        table = db.company
    elif request.args(1) == 'locations':
        table = db.locations
    elif request.args(1) == 'people':
        table = db.people
    elif request.args(1) == 'events':
        table = db.event
    elif request.args(1) == 'people_type':
        table = db.people_type
    elif request.args(1) == 'social_media':
        table = db.social_media
    form = SQLFORM(table, id)
    return locals()

def edit_event():
    id = request.args(0, cast=int)
    form = SQLFORM(db.events,id)
    return locals()

def event_type_show():
    id = request.args(0, cast=int)
    if request.args(1) == 'event_type':
        query = db.event_type.id == id
    elif request.args(1) == 'states':
        query = db.states.id == id
    elif request.args(1) == 'company':
        query = db.company.id == id
    elif request.args(1) == 'locations':
        query = db.locations.id == id
    elif request.args(1) == 'people':
        query = db.people.id == id
    elif request.args(1) == 'events':
        query = db.event.id == id
    elif request.args(1) == 'people_type':
        query = db.people_type.id == id
    elif request.args(1) == 'social_media':
        query = db.social_media.id == id
    rows = db(query).select()
    return locals()

def delete():
    id = request.args(0, cast=int)
    if request.args(1) == 'event_type':
        query = db.event_type.id == id
    elif request.args(1) == 'states':
        query = db.states.id == id
    elif request.args(1) == 'company':
        query = db.company.id == id
    elif request.args(1) == 'locations':
        query = db.locations.id == id
    elif request.args(1) == 'people':
        query = db.people.id == id
    elif request.args(1) == 'events':
        query = db.event.id == id
    elif request.args(1) == 'people_type':
        query = db.people_type.id == id
    elif request.args(1) == 'social_media':
        query = db.social_media.id == id
    delete_row = db(query).delete()
    response.flash = 'deleted'
    return locals()

def index():
    rows = db(db.people.location_id == db.locations.id).select(db.locations.state_name,db.people.id.count(),groupby=db.locations.state_name)
    rows2 = db(db.events).select(db.events.event_id,db.events.id.count(),groupby=db.events.event_id)
    return locals()

def search():
    word = request.vars.search
#     states = db((db.states.code.contains(word)) | (db.states.state_name.contains(word))).select()
    companies = db((db.company.name.contains(word)) | (db.company.industry.contains(word)) | (db.company.main_location.contains(word)) | (db.company.website.contains(word)) | (db.company.main_phone_number.contains(word)) | (db.company.sales_rep.contains(word))| (db.company.linkedin.contains(word))| (db.company.twitter.contains(word))| (db.company.facebook.contains(word))).select()
#     event_types = db((db.event_type.event_name.contains(word)) | (db.event_type.description.contains(word))).select()
#     events = db((db.events.status.contains(word)) | (db.events.notes.contains(word))).select()
#     people_types = db((db.people_type.people_type.contains(word))).select()
    people = db((db.people.first_name.contains(word)) | (db.people.last_name.contains(word)) | (db.people.email.contains(word)) | (db.people.phone_number.contains(word)) | (db.people.office_phone.contains(word)) | (db.people.title.contains(word)) | (db.people.role.contains(word)) | (db.people.address.contains(word))| (db.people.linkedin.contains(word))| (db.people.twitter.contains(word))| (db.people.facebook.contains(word))).select()
#     locations = db((db.locations.name.contains(word)) | (db.locations.address.contains(word)) | (db.locations.city.contains(word)) | (db.locations.zip_code.contains(word)) | (db.locations.main_phone_number.contains(word))).select()
    no_result = f'No result for "{word}"'
    return locals()

def search2():
    id = request.args(0, cast=int)
    name = request.args(1)
    referer = request.env.http_referer.replace("http://127.0.0.1:8000/cddeX/default/", "")
    events = db(db.events.person_id == id).select()
    no_result = f'No event for "{name}"'
    return locals()

def search3():
    id = request.args(0, cast=int)
    name = request.args(1)
    referer = request.env.http_referer.replace("http://127.0.0.1:8000/cddeX/default/", "")
    locations = db(db.locations.company_id == id).select()
    no_result = f'No location for "{name}"'
    return locals()

def about():
    return locals()

@auth.requires_login()
def states():
    states = SQLFORM.grid(db.states)
    return locals()

@auth.requires_login()
def company():
    company = SQLFORM.grid(db.company)
    return locals()

@auth.requires_login()
def event_type():
    event_type = SQLFORM.grid(db.event_type)
    return locals()

@auth.requires_login()
def events():
    grid = SQLFORM.grid(db.events)
    return locals()

@auth.requires_login()
def people_type():
    grid = SQLFORM.grid(db.people_type)
    return locals()
    
@auth.requires_login()
def locations():
    grid = SQLFORM.grid(db.locations)
    return locals()
    
@auth.requires_login()
def people():
    grid = SQLFORM.grid(db.people)
    return locals()

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
