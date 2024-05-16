class PromptTemplateSelector:
    def __init__(self):
        self.templates = {
            'task1':{
                'role1': 'Template for task1 and role1',
                'role2': 'Template for task1 and role2',
            },
            'task2':{
                'role1': 'Template for task2 and role1',
                'role2': 'Template for task2 and role2',
            },
        }

    def get_template(self, task, role):
        """Retrieve the prompt template based on the task and role."""
        task_templates = self.templates.get(task)
        if not task_templates:
            return None
        return task_templates.get(role, task_templates.get('default'))