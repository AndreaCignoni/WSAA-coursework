
# This Python code snippet is designed to interact with an XML document using the DOM (Document Object Model) parser. 

# The XML document is assumed to contain information about employees, with each employee represented as an "Employee" element.

# The code retrieves a NodeList of all "Employee" elements from the XML document using the getElementsByTagName method. 

# It then prints the total number of "Employee" elements found using the len() function.

# Subsequently, the code iterates through each "Employee" element in the NodeList using a for loop. 

# Within the loop, you can access and manipulate the properties and child elements of each employeeNode as needed.

# Note: Before using this code, ensure that 'doc' represents a valid XML Document object,

# and the XML document structure conforms to the expected format with "Employee" elements.

import xml.dom.minidom

# Load the XML file into a Document object
xml_file_path = "employee.xml"
doc = xml.dom.minidom.parse(xml_file_path)

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList)) # The len() function is used here to determine the total number of "Employee" elements in the XML document.
# The len() function is then applied to the NodeList, providing the count of "Employee" elements.
for employeeNode in employeeNodeList:
    #  Within the loop, firstNameNode will be assigned the first occurrence of the "FirstName" element for each employee, allowing you to access and manipulate its data.
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    # Extract the text content of "FirstName" and remove leading/trailing whitespace
    firstName = firstNameNode.firstChild.nodeValue.strip()

    print(firstName)