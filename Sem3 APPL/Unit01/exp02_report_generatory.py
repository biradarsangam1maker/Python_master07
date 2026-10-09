class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, func):
        cls.templates[name] = func

    @classmethod
    def get_template(cls, name):
        if name in cls.templates:
            return cls.templates[name]
        else:
            return None

    def __str__(self):
        return "Title: " + self.title + "\nContent: " + self.content

    def __call__(self, name):
        func = self.get_template(name)

        if func == None:
            return "Template not found"

        return func(self)


def bold_text(func):
    def wrapper(report):
        return "***" + func(report) + "***"
    return wrapper


def simple_template(report):
    return "--- " + report.title + " ---\n" + report.content


@bold_text
def fancy_template(report):
    return "FANCY REPORT: " + report.title + " | Data: " + report.content


Report.add_template("simple", simple_template)
Report.add_template("fancy", fancy_template)

report = Report("May 2026 Library Summary",
                "50 new users registered.")

print(report)
print(report("simple"))
print(report("fancy"))
print(report("ghost"))
