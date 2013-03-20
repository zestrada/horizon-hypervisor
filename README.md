horizon-hypervisor
==================

Plugin for openstack dashboard that presents hypervisor information from nova

Currently implemented as a panel for the admin dashboard

To install, simply copy the contents of panel to $HORIZONPATH/openstck-dashboard/dashboards/admin/ (creating a subdirectory 'hypervisors')

then modify dashboard.py to add the new panel:
```python
    panels = ('overview', 'instances', 'volumes', 'flavors',
              'images', 'projects', 'users', 'networks', 'routers', 'info',
              'hypervisors')
```
