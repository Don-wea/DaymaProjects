from views.module_dashboard.module_dashboard import ModuleDashboard
from views.module_inventory.module_inventory import ModuleInventory
from views.module_sales.module_sales import ModuleSales
from views.module_customers.module_customers import ModuleCustomers
from views.module_settings.module_settings import ModuleSettings

# Function to return the correct module content based on the module name
def get_module_content(module_name, page):
    if module_name == "dashboard":
        return ModuleDashboard(page)
    elif module_name == "inventory":
        return ModuleInventory(page)
    elif module_name == "sales":
        return ModuleSales(page)
    elif module_name == "customers":
        return ModuleCustomers(page)
    elif module_name == "settings":
        return ModuleSettings(page)
    else:
        return None