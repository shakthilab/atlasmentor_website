import subprocess, os, json, time

routes = [
    ('/', 'homepage', 'Homepage'),
    ('/tashkent-medical-academy', 'university_tashkent', 'Tashkent Medical Academy'),
    ('/samarkand-state-medical-institute', 'university_samarkand', 'Samarkand State Med Inst'),
    ('/study-mbbs-in-uzbekistan-for-indian-students', 'guide_uzbekistan', 'Study MBBS Uzbekistan Guide'),
    ('/mbbs-university/georgia', 'listing_georgia', 'Georgia Universities Listing'),
    ('/contact-us', 'contact_us', 'Contact Us'),
    ('/alte-medical-university', 'university_alte', 'Alte Medical University')
]

os.makedirs('scratch/lh_prod_live', exist_ok=True)

for path, key, name in routes:
    url = f'https://atlasmentor.com{path}'
    
    # 1. Mobile Audit
    mob_out = f'scratch/lh_prod_live/{key}_mobile.json'
    if not os.path.exists(mob_out):
        print(f'Auditing Mobile: {url} ...')
        cmd_mob = f'npx -y lighthouse \"{url}\" --output=json --output-path=\"{mob_out}\" --only-categories=performance,accessibility,best-practices,seo --form-factor=mobile --screenEmulation.mobile=true --chrome-flags=\"--headless\"'
        subprocess.run(cmd_mob, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

    # 2. Desktop Audit
    dt_out = f'scratch/lh_prod_live/{key}_desktop.json'
    if not os.path.exists(dt_out):
        print(f'Auditing Desktop: {url} ...')
        cmd_dt = f'npx -y lighthouse \"{url}\" --output=json --output-path=\"{dt_out}\" --only-categories=performance,accessibility,best-practices,seo --form-factor=desktop --screenEmulation.mobile=false --chrome-flags=\"--headless\"'
        subprocess.run(cmd_dt, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

print('All Live Production Lighthouse audits completed!')
