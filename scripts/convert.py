import subprocess

def convert_docx_to_md(docx_file, md_file, custom_lines):
    # Convert the .docx file to .md using Pandoc
	# include word styles in md
	# github flavored markdown
	# ../Resume/> pandoc -f docx+styles -t gfm sebvc_Resume.docx -o sebvc_Resume.md
    pandoc_command = ['pandoc', '-f', 'docx+styles', '-t', 'gfm', docx_file, '-o', md_file]
    subprocess.run(pandoc_command)

    # Read the content of the generated .md file
    with open(md_file, 'r') as file:
        content = file.read()

    # Insert the custom lines at the beginning of the content
    custom_lines = '\n'.join(custom_lines)
    content_with_custom_lines = f"{custom_lines}\n{content}"

    # Write the modified content back to the .md file
    with open(md_file, 'w') as file:
        file.write(content_with_custom_lines)

# Specify the paths and custom lines
docx_file_path = 'sebvc_Resume.docx'
md_file_path = 'sebvc_Resume.md'
custom_lines = [
	'<!-- Python file.write() to include .CSS reference -->',
    '<head>',
    '  <link rel="stylesheet" href="media/style_block_insert.css">',
    '</head>',
	'<!--------------------------------------------------->'
    ]

# Call the conversion function
convert_docx_to_md(docx_file_path, md_file_path, custom_lines)
