from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from reports.historical import Historical
from reports.report_details import REGION_COUNTRY_MAP, get_countries


class Command(BaseCommand):
    help = 'Import historical GMMP data from an XLSX file'
    option_list = BaseCommand.option_list + (
        make_option('--global',
            action='store_true',
            help='Coverage is global'),
        make_option('--region REGION',
            action='store',
            dest='region',
            help='Import historical data for a region. One of: %s' % ', '.join(sorted(REGION_COUNTRY_MAP.keys()))),
        make_option('--country COUNTRY',
            action='store',
            dest='country',
            help='Import historical data for a country. One of: %s' % ', '.join(sorted(c[0] for c in get_countries()))),
    )

    def handle(self, *args, **options):
        historical = Historical()
        coverage = None
        region = None
        country = None

        if options['global']:
            coverage = 'global'
        elif options['region']:
            coverage = 'region'
            region = options['region']

            if region not in REGION_COUNTRY_MAP:
                raise ValueError("Unknown region: %s" % region)

        elif options['country']:
            coverage = 'country'
            country = options['country']

            countries = {c: n for c, n in get_countries()}

            if not country.upper() in countries:
                for code, name in countries.items():
                    if name.upper() == country:
                        country = code
                        break

                if not country in countries:
                    raise ValueError("Unknown country: %s" % country)

        else:
            raise CommandError("Must specify --global or --region")

        for fname in args:
            historical.import_from_file(fname, coverage, region=region, country=country)

        historical.save()
