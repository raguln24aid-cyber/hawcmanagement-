import frappe

def setup():
    # 1. Create Module Def
    if not frappe.db.exists("Module Def", "HAWC Management"):
        mod = frappe.new_doc("Module Def")
        mod.module_name = "HAWC Management"
        mod.app_name = "hawc_management"
        mod.insert(ignore_permissions=True)
        print("Created Module: HAWC Management")

    # 2. Create Student Lead DocType
    if not frappe.db.exists("DocType", "Student Lead"):
        doc = frappe.new_doc("DocType")
        doc.name = "Student Lead"
        doc.module = "HAWC Management"
        doc.custom = 0
        doc.istable = 0
        doc.is_submittable = 0
        
        doc.append("fields", {"fieldname": "student_name", "label": "Student Name", "fieldtype": "Data", "reqd": 1})
        doc.append("fields", {"fieldname": "mobile_number", "label": "Mobile Number", "fieldtype": "Phone", "reqd": 1, "unique": 1})
        doc.append("fields", {"fieldname": "email", "label": "Email", "fieldtype": "Data", "unique": 1})
        doc.append("fields", {"fieldname": "city", "label": "City", "fieldtype": "Data"})
        doc.append("fields", {"fieldname": "course_interested", "label": "Course Interested", "fieldtype": "Select", "options": "\nB.Tech\nM.Tech\nBCA\nMCA"})
        doc.append("fields", {"fieldname": "lead_source", "label": "Lead Source", "fieldtype": "Select", "options": "\nWebsite\nWalk-in\nPhone\nWhatsApp\nFacebook\nInstagram\nReferral\nOther"})
        doc.append("fields", {"fieldname": "lead_status", "label": "Lead Status", "fieldtype": "Select", "options": "New\nContacted\nInterested\nFollow Up\nAdmitted\nRejected", "default": "New"})
        doc.append("fields", {"fieldname": "assigned_counsellor", "label": "Assigned Counsellor", "fieldtype": "Link", "options": "User"})
        doc.append("fields", {"fieldname": "remarks", "label": "Remarks", "fieldtype": "Small Text"})
        
        doc.insert(ignore_permissions=True)
        print("Created DocType: Student Lead")

    # 3. Create Follow Up DocType
    if not frappe.db.exists("DocType", "Follow Up"):
        doc = frappe.new_doc("DocType")
        doc.name = "Follow Up"
        doc.module = "HAWC Management"
        doc.custom = 0
        
        doc.append("fields", {"fieldname": "student_lead", "label": "Student Lead", "fieldtype": "Link", "options": "Student Lead", "reqd": 1})
        doc.append("fields", {"fieldname": "follow_up_date", "label": "Follow-up Date", "fieldtype": "Date", "reqd": 1})
        doc.append("fields", {"fieldname": "counsellor", "label": "Counsellor", "fieldtype": "Link", "options": "User"})
        doc.append("fields", {"fieldname": "notes", "label": "Notes", "fieldtype": "Text"})
        doc.append("fields", {"fieldname": "next_follow_up", "label": "Next Follow-up", "fieldtype": "Date"})
        doc.append("fields", {"fieldname": "status", "label": "Status", "fieldtype": "Select", "options": "Pending\nCompleted", "default": "Pending"})
        
        doc.insert(ignore_permissions=True)
        print("Created DocType: Follow Up")

    # 4. Create Admission DocType
    if not frappe.db.exists("DocType", "Admission"):
        doc = frappe.new_doc("DocType")
        doc.name = "Admission"
        doc.module = "HAWC Management"
        doc.custom = 0
        
        doc.append("fields", {"fieldname": "student_lead", "label": "Student Lead", "fieldtype": "Link", "options": "Student Lead", "reqd": 1})
        doc.append("fields", {"fieldname": "admission_date", "label": "Admission Date", "fieldtype": "Date", "reqd": 1})
        doc.append("fields", {"fieldname": "course", "label": "Course", "fieldtype": "Data", "reqd": 1})
        doc.append("fields", {"fieldname": "fees", "label": "Fees", "fieldtype": "Currency"})
        doc.append("fields", {"fieldname": "payment_status", "label": "Payment Status", "fieldtype": "Select", "options": "Pending\nPartial\nPaid", "default": "Pending"})
        
        doc.insert(ignore_permissions=True)
        print("Created DocType: Admission")

    frappe.db.commit()
    print("All DocTypes setup successfully!")

setup()
