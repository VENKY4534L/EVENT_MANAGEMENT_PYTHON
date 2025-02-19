import streamlit as st

# Initialize events if not already in session state
if 'events' not in st.session_state:
    st.session_state.events = [{"id": 1, "name": "Birthday Party"}, {"id": 2, "name": "Conference"}]

def view_events():
    st.subheader("View Events")
    if not st.session_state.events:
        st.write("No events to display.")
    else:
        for event in st.session_state.events:
            st.write(f"ID: {event['id']}, Name: {event['name']}")

def add_event():
    st.subheader("Add Event")
    event_name = st.text_input("Enter Event Name")
    if st.button("Add Event"):
        if event_name:  # Check if event name is not empty
            new_id = len(st.session_state.events) + 1
            st.session_state.events.append({"id": new_id, "name": event_name})
            st.success(f"Event '{event_name}' added successfully!")
        else:
            st.error("Event name cannot be empty!")

def update_event():
    st.subheader("Update Event")
    event_id = st.number_input("Enter Event ID to Update", min_value=1, step=1)
    new_name = st.text_input("Enter New Event Name")
    if st.button("Update Event"):
        for event in st.session_state.events:
            if event["id"] == event_id:
                event["name"] = new_name
                st.success(f"Event ID {event_id} updated successfully!")
                break
        else:
            st.error("Event ID not found!")

def delete_event():
    st.subheader("Delete Event")
    event_id = st.number_input("Enter Event ID to Delete", min_value=1, step=1)
    if st.button("Delete Event"):
        st.session_state.events = [event for event in st.session_state.events if event["id"] != event_id]
        st.success(f"Event ID {event_id} deleted successfully!")

# Main App
st.title("Event Management")
menu = st.sidebar.selectbox("Menu", ["View Events", "Add Event", "Update Event", "Delete Event"])

if menu == "View Events":
    view_events()
elif menu == "Add Event":
    add_event()
elif menu == "Update Event":
    update_event()
elif menu == "Delete Event":
    delete_event()
