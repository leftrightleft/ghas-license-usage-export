# ghas-license-usage-export
This Action queries the enterprise GitHub API in your environment and returns a complete list of GitHub Advanced Security committers, including counts as a JSON document.  

## How does it work?
1. The action is triggered
2. The action calls your endpoint for the [billing api](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/billing?apiVersion=2022-11-28#get-github-advanced-security-active-committers-for-an-enterprise)
3. A JSON doc is uploaded as an artifact from the action run

## How do I use it?
### Prep the Action for your environment
1. Fork this repo into your environment
2. Provision a new PAT that has `admin:enterprise` scope.  **NOTE:** You need to create this PAT as an enterprise admin
3. Add a new Actions secret called `ENT_ADMIN_TOKEN` and set your newly created PAT as that secret
4. Edit [export-ghas-users.yml](.github/workflows/export-ghas-users.yml) and add your enterprise name and api endpoint in this section:
   ```
         - name: Get billers
        run: |
          # execute python script
          python get-billers.py 
        env:
          API_ENDPOINT: "api.github.com"
          ENTERPRISE_NAME: "burrito-party"
          ADMIN_TOKEN: ${{ secrets.ENT_ADMIN_TOKEN }}
   ```

### Execute the action
This action is triggered using two methods.  One is a cron.  You can edit the `schedule:` in the workflow file to match your needs.  Otherwise, you can manually trigger this workflow by navigating to **Actions** > **GHAS Billing Export** then choose "Run workflow"
<img width="1200" alt="image" src="https://github.com/leftrightleft/ghas-license-usage-export/assets/4910518/f00b2f00-e69d-4fb6-b6e9-a3b31cef2695">

### View results
After the action is run, we upload the result from the API as a JSON document as an action artifact.  Navigate to the last actions run and download the file from the "Artifacts" section.
<img width="1190" alt="image" src="https://github.com/leftrightleft/ghas-license-usage-export/assets/4910518/cadbeabf-f0ae-431d-b5db-077e24d73954">

