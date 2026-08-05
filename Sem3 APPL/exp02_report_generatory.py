class Report:
    templates = {}
    def __init__(self,title,content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls,template_name,template_func):
        cls.templates[template_name] = template_func

    @classmethod
    def get_template(cls,template_name):
        template = cls.templates.get(template_name)
        if template == None:
            return f'{template_name} template not found in the dictionary'
        else:
            return template

    def __str__(self):
        return f'Title:{self.title} \n Content:{self.content}'
    
    def __call__(self,template_name):
        template_func = self.get_template(template_name)
        if callable(template_func):
            return template_func(self)
        else:
            return f"{template_name} template not found."
        

def bold_text(func):
        def wrapper(report_instance):
            raw_text = func(report_instance)
            return f'***{raw_text}***'
        return wrapper

def simple_template(report_instance):
    ans =f'--- {report_instance.title} ---\n{report_instance.content}'
    return ans

@bold_text
def fancy_template(report_instance):
    return f'FANCY REPORT: {report_instance.title} | Data: {report_instance.content}'

if __name__=="__main__":
    Report.add_template("simple",simple_template)
    Report.add_template("fancy",fancy_template)

    library_report = Report("May 2026 Library Summary","50 new users registered.")

    print("\n--- Testing Standart Output ---")
    print(library_report)

    print("\n--- Testing Decorated Fancy Template ---")
    print(library_report("fancy"))

    print("\n--- Testing Defensive Error Handling ---")
    print(library_report("ghost_template"))
    print(Report.templates)
