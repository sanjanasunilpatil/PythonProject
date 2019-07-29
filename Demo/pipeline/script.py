from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
from datetime import datetime, timedelta
import time
import os


class script:
    def print_item(self, group):
        """Print an Azure object instance."""
        print("\tName: {}".format(group.name))
        print("\tId: {}".format(group.id))
        if hasattr(group, 'location'):
            print("\tLocation: {}".format(group.location))
        if hasattr(group, 'tags'):
            print("\tTags: {}".format(group.tags))
        if hasattr(group, 'properties'):
            self.print_properties(group.properties)
        print("\n")

    def print_properties(self, props):
        """Print a ResourceGroup properties instance."""
        if props and hasattr(props, 'provisioning_state') and props.provisioning_state:
            print("\tProperties:")
            print("\t\tProvisioning State: {}".format(props.provisioning_state))
        print("\n")

    def print_activity_run_details(self, activity_run):
        """Print activity run details."""
        print("\n\tActivity run details\n")
        print("\tActivity run status: {}".format(activity_run.status))
        if activity_run.status == 'Succeeded':
            print("\tNumber of bytes read: {}".format(
                activity_run.output['dataRead']))
            print("\tNumber of bytes written: {}".format(
                activity_run.output['dataWritten']))
            print("\tCopy duration: {}".format(
                activity_run.output['copyDuration']))
        else:
            print("\tErrors: {}".format(activity_run.error['message']))

    def connectivity(self):
        # Azure subscription ID
        subscription_id = '540bcf3e-716f-4ab5-b499-68e5285ea954'

        rg_name = 'rg1Sanjana'
        df_name = 'dfSanjana'

        # Specify your Active Directory client ID, client secret, and tenant ID
        credentials = ServicePrincipalCredentials(client_id='720226fd-782c-4068-a00c-63f3680dc133',
                                                  secret='2Y:Hc?0YauQZ8*IX3=ppT1/E*@@=T2hM',
                                                  tenant='524b0e96-35a3-46ef-ade3-a76c1936a890')
        resource_client = ResourceManagementClient(credentials, subscription_id)
        adf_client = DataFactoryManagementClient(credentials, subscription_id)

        return resource_client, adf_client, rg_name, df_name

    def createResourceGroup(self):

        client = self.connectivity()
        rg_params = {'location': 'eastus2'}
        rg_name = client[2]

        client[0].resource_groups.create_or_update(rg_name, rg_params)

    def createDataFactory(self):

        df_resource = Factory(location='eastus2')

        client = self.connectivity()

        df = client[1].factories.create_or_update(client[2], client[3], df_resource)
        self.print_item(df)
        while df.provisioning_state != 'Succeeded':
            df = client[1].factories.get(client[2], client[3])
            time.sleep(1)

    def storageLinkedService(self):

        ls_name = 'storageLinkedService-Sanjana'

        storage_string = SecureString('DefaultEndpointsProtocol=https;AccountName=strsanjana;AccountKey=1bHSpeYu3sah6kf4XsTAaZyirb3Ah2XGafYZmjkq5ykUqjpQp+X8TXQuziwKvGL1sFVoyHqkSdcJtCvc4TZKnQ==')

        client = self.connectivity()

        ls_azure_storage = AzureStorageLinkedService(connection_string=storage_string)

        ls = client[1].linked_services.create_or_update(client[2], client[3], ls_name, ls_azure_storage)
        self.print_item(ls)


    def createBlobDataset(self, blob_path, blob_filename):

        ls_name = 'storageLinkedService-Sanjana'
        ds_name = 'dataset'
        client = self.connectivity()
        ds_ls = LinkedServiceReference(ls_name)

        if len(blob_filename) is 0:
            ds_azure_blob = AzureBlobDataset(ds_ls, folder_path=blob_path)
        else:
            ds_azure_blob = AzureBlobDataset(ds_ls, folder_path=blob_path, file_name=blob_filename)

        ds = client[1].datasets.create_or_update(client[2], client[3], ds_name, ds_azure_blob)
        self.print_item(ds)

        return ds_name


    def copyActivityBlobToBlob(self):

        act_name = 'copyBlobToBlob'

        blob_source = BlobSource()
        blob_sink = BlobSink()
        dsin_ref = DatasetReference(self.createBlobDataset('cnt1/input', 'input.txt'))
        dsOut_ref = DatasetReference(self.createBlobDataset('cnt1/output', ''))
        copy_activity = CopyActivity(act_name, inputs=[dsin_ref], outputs=[dsOut_ref], source=blob_source, sink=blob_sink)

        return copy_activity

    def createPipelineCopyActivity(self):

        # Create a pipeline with the copy activity
        p_name = 'copyPipeline'
        params_for_pipeline = {}

        client = self.connectivity()
        copy_activity = self.copyActivityBlobToBlob()
        p_obj = PipelineResource(activities=[copy_activity], parameters=params_for_pipeline)
        p = client[1].pipelines.create_or_update(client[2], client[3], p_name, p_obj)
        self.print_item(p)

        # Create a pipeline run
        run_response = client[1].pipelines.create_run(client[2], client[3], p_name, {})

        # Monitor the pipeline run
        time.sleep(30)
        pipeline_run = client[1].pipeline_runs.get(client[2], client[3], run_response.run_id)
        print("\n\tPipeline run status: {}".format(pipeline_run.status))
        activity_runs_paged = list(client[1].activity_runs.list_by_pipeline_run(client[2], client[3], pipeline_run.run_id, datetime.now() - timedelta(1), datetime.now() + timedelta(1)))
        self.print_activity_run_details(activity_runs_paged[0])


    def createADLSLinkedService(self):

        client = self.connectivity()
        ls_name = 'ADLSLinkedService'

        ls_azure_storage = AzureDataLakeStoreLinkedService(
            data_lake_store_uri='adl://sanjanaadls.azuredatalakestore.net/',
            service_principal_id='720226fd-782c-4068-a00c-63f3680dc133',
            service_principal_key='2Y:Hc?0YauQZ8*IX3=ppT1/E*@@=T2hM')

        client[1].linked_services.create_or_update(client[2], client[3], ls_name, ls_azure_storage)


s = script()
# s.createResourceGroup()
s.createDataFactory()
# s.storageLinkedService()
# s.createPipelineCopyActivity()

s.createADLSLinkedService()



