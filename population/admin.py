from colonialismdb.population.models import MainDataEntry
from colonialismdb.common.admin import BaseSubmitAdmin
from django.contrib import admin

class MainDataEntryAdmin(BaseSubmitAdmin) :
  fieldsets = [
      (None,
        {'fields' : ['active', 'submitted_by']}),

      ('Location Information', 
        {'fields' : ['location', 'original_location_name', 'alternate_location_name']}),
      
      ('Date Range', 
        {'fields' : ['begin_date', 'end_date']}),

      ('Population Characteristics', 
        {'fields' : ['religion', 'race', 'ethnicity', 'ethnic_origin', 'age_start', 'age_end', 'population_condition']}),

      ('Population Statistics', 
        {'fields' : ['individuals_population_value', 'families_population_value', 'male_population_value', 'female_population_value', 'value_unit', 'is_total']}),

      ('Source Information', 
        {'fields' : ['source_id', 'combined_id', 'page_num', 'polity', 'iso', 'wb']}),

      ('Other Information', 
        {'fields' : ['remarks', ], 'classes' : ['collapse', ]}),
  ]

  list_display = ('location', 'begin_date', 'end_date', 'active', 'submitted_by')
  ordering = ['begin_date']

  activate_perm = 'population.activate_main_data_entry'


admin.site.register(MainDataEntry, MainDataEntryAdmin)