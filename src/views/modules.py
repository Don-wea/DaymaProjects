from views.module_dashboard.module_dashboard import moduleDashboard
from views.module_inventory.module_inventory import moduleInventory
from views.module_sales.module_sales import moduleSales
from views.module_customers.module_customers import moduleCustomers
from views.module_settings.module_settings import moduleSettings

# Function to return the correct module content based on the module name
def get_module_content(module_name):
    if module_name == "dashboard":
        return moduleDashboard()
    elif module_name == "inventory":
        return moduleInventory()
    elif module_name == "sales":
        return moduleSales()
    elif module_name == "customers":
        return moduleCustomers()
    elif module_name == "settings":
        return moduleSettings()
    else:
        return None
