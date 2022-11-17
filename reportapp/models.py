from django.db import models


# reject_status =(('Specimen', 'Specimen'),('Damaged','Damaged'), ('Sample','Sample'),('Challenged','Challenged')
#             , ('Teach','Teach'), ('In Process','In Process'), ('Rejected By Camera','Rejected By Camera')
#             , ('Unused','Unused'), ('Returned Number','Returned Number'), ('Downloaded Quality', 'Downloaded Quality'))
class ProductionReport(models.Model):
    id = models.AutoField(primary_key=True)
    process_order_number = models.CharField(max_length=100, default="process order number")
    batch_number = models.CharField(max_length=100, default="batch number", unique=True)
    product_name = models.CharField(max_length=100, default="product name")
    manufacture_loc_name = models.CharField(max_length=100, default="manufacture location name")
    line_name = models.CharField(max_length=100, default="line name")
    system_name = models.CharField(max_length=100, default="system name")
    created_by = models.CharField(max_length=100, default="created by")
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)

    def __str__(self):
        return self.batch_number