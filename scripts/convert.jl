# Import the `run` function from the `Base` module
import Base.run

# Define the file paths
docx_file = "sebvc_Resume.docx"
md_file = "sebvc_Resume.md"

# Convert .docx to .md using Pandoc
run(`pandoc -f docx -t markdown_mmd $docx_file -o $md_file`)

# Read the contents of the .md file
md_content = read(md_file, String)

# Define the custom lines to add at the beginning, I am on Windows Hence the use of \r\n to write
custom_lines = """<head>\r\n  <link rel="stylesheet" href="media/style_block_insert.css">\r\n</head>\r\n"""

# Prepend the custom lines to the existing content
md_content = custom_lines * md_content

# Write the updated content back to the .md file
write(md_file, md_content)
