# This is to test the library.
from dynamics import contacts

if __name__ == '__main__':
    # Replace these variables with your actual values
    tenant_id = 'tenant_id'
    client_id = 'client_id'
    client_secret = 'client_secret'
    tenant_name = 'tenant_name'
    crm_url = f"https://{tenant_name}.crm4.dynamics.com/"

    # Create Access Token
    access_token = contacts.accessToken(tenant_id, client_id, client_secret, crm_url)

    # Search for a contact
    search_params = {
        "firstname": "Mustafa",
        "lastname": "Abusalah",
        "emailaddress1": "ma.abusalah@gmail.com"
    }
    return_fields = "firstname,lastname,emailaddress1,mobilephone"
    crm_contacts = contacts.search_contacts(crm_url, access_token, search_params, return_fields)
    print(crm_contacts)

    """ 
    Create new contact normal profile
    Contact data that you want to add, feel free to add whatever data you have.
    You may find on the below link Dataverse Dynamics Contact default fields:
    https://learn.microsoft.com/es-es/power-apps/developer/data-platform/webapi/reference/contact?view=dataverse-latest&viewFallbackFrom=dynamics-ce-odata-9
    """
    contact_data = {
        "firstname": "fname",
        "lastname": "lname",
        "birthdate": "%Y-%m-%d",
        "emailaddress1": "email",
        "mobilephone": "12345678"
    }
    # Add contact to Dataverse
    add_crm_contact = contacts.add_contact(contact_data, crm_url, access_token)

    # Update contracts
    update_data = {
        "firstname": "fname",
        "lastname": "lname"
    }
    contact_id= '' # Replace with the actual contact ID
    updated_crm_contact = contacts.update_contact(access_token, contact_id, update_data, crm_url)

    # Delete Contact

    contact_id = ''  # Replace with the actual contact ID.

    deleted = contacts.delete_contact(crm_url, access_token, contact_id)
    if deleted:
        print("Contact deleted successfully")
    else:
        print("Error deleting contact")