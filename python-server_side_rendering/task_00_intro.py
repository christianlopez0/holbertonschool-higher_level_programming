def generate_invitations(template, attendees):
    import os
    
    # Check if template is a string and attendees is a list of dictionaries
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee's data
        invitation_content = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )
        
        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(invitation_content)
        
        print(f"Generated {filename}")

# Example usage
if __name__ == "__main__":
    # Read the template from file
    with open('invitationtemplate.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Generate invitations
    generate_invitations(template_content, attendees)
