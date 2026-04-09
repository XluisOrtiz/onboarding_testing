# 🗺️ Visual Product Map (Intel Onboarding)

Este mapa se actualiza localmente. Haz clic en los nodos para ir a la documentación.

```mermaid
graph LR
    classDef category fill:#0071C5,stroke:#fff,stroke-width:2px,color:#fff,font-weight:bold;
    classDef product fill:#f4f4f4,stroke:#0071C5,stroke-width:1px,color:#333;
    CaaSADUsers([CaaS AD Users]):::category --> BasicaccessforCaaS0["Basic access for CaaS"]:::product
    CaaSITScoverityuatProjectOwner([CaaS ITS coverity-uat Project Owner]):::category --> DedicatedCoverityCluster2["Dedicated Coverity Cluster"]:::product
    click DedicatedCoverityCluster2 "https://amr.caas.intel.com/" "Abrir Wiki"
    CaasITScoverityDeveloper([Caas ITS coverity Developer]):::category --> RepoaccessinCaaSHarbor4["Repo access in CaaS Harbor"]:::product
    click RepoaccessinCaaSHarbor4 "https://amr-its-registry.caas.intel.com/" "Abrir Wiki"
    DevToolsArtifactoryCoverityUBITAFORProjectAdministrator([DevTools - Artifactory - Coverity - UBIT-AF-OR - Project Administrator]):::category --> ArtifactoryRepoforuploadingcli6["Artifactory Repo for uploading client installer, license, product documentation and sample code for testing, etc."]:::product
    click ArtifactoryRepoforuploadingcli6 "https://ubit-artifactory-or.intel.com/ui/repos/tree/General/coverity-or-local" "Abrir Wiki"
    PrivilegedAdminGroupAccessPLCSCodeScanningAdmins([Privileged Admin Group Access - PLCS Code Scanning Admins]):::category --> Requiredforjumpserveraccess9["Required for jump server access"]:::product
    ITCollaboratorEDAdministrativeSystemAccess([IT Collaborator ED Administrative System Access]):::category --> Requiredforworkernodeaccess10["Required for worker node access"]:::product
    CaaSITScoverityProjectOwner([CaaS ITS coverity Project Owner]):::category --> ProjectaccessinCaaSITScluser12["Project access in CaaS ITS cluser"]:::product
    click ProjectaccessinCaaSITScluser12 "https://amr.caas.intel.com/" "Abrir Wiki"
    ServiceNowCloudCodeScanKA([ServiceNow Cloud Code Scan KA]):::category --> RequiredtoenterandviewServiceN15["Required to enter and view Service Now, as well as queue and knowledge article access."]:::product
    DevToolsProtexsupportL3([DevTools - Protex_support - L3]):::category --> GrantsaccesstoProtexwikiadmini20["Grants access to Protex wiki administration section"]:::product
    FullAdminAccesstoAWSAccount772743572118([Full Admin Access to AWS Account 772743572118]):::category --> BDBAAWSaccess22["BDBA AWS access"]:::product
    eGRCProductionGeneralAccessADCORP([eGRC Production General Access_AD-CORP]):::category --> AccesstoeGRC25["Access to eGRC"]:::product
    ITJiraUsersProd([IT Jira Users Prod]):::category --> AccesstoourJiraboard27["Access to our Jira board"]:::product
    PAMAdminAccountCorp([PAM Admin Account Corp]):::category --> Grantsaccesstoourpasswordmanag29["Grants access to our password management platform"]:::product
    PAMAAMSafeOwnerforCNCITSCANOPSPR([PAM AAM Safe Owner for CNC ITSCANOPS PR]):::category --> NewPAMsafe31["New PAM safe"]:::product
    1SourceGithubUser([1Source Github User]):::category --> GrantsaccesstoGithub34["Grants access to Github"]:::product
    ITScanTeamGitHub([IT Scan Team GitHub]):::category --> AccesstoScanGithub35["Access to Scan Github"]:::product
    DynatraceIAP35826Admin([Dynatrace - IAP 35826 - Admin]):::category --> DynatraceCoverity37["Dynatrace - Coverity"]:::product
    DynatraceIAP6638Admin([Dynatrace - IAP 6638  - Admin]):::category --> DynatraceProtex38["Dynatrace - Protex"]:::product
    DynatraceIAP21706Admin([Dynatrace - IAP 21706 - Admin]):::category --> DynatraceBDBA39["Dynatrace - BDBA"]:::product
    DynatraceIAP6639Admin([Dynatrace - IAP 6639 - Admin]):::category --> DynatraceKlocwork40["Dynatrace - Klocwork"]:::product
    DynatraceIAP23551Admin([Dynatrace - IAP 23551 - Admin]):::category --> DynatraceRecordCenter41["Dynatrace - Record Center"]:::product
    DynatraceIAP9067Admin([Dynatrace - IAP 9067 - Admin]):::category --> DynatraceCollaborator42["Dynatrace - Collaborator"]:::product
    AAPlatformECKCoverityReadonly([AAPlatform - ECK - Coverity - Readonly]):::category --> ECKCoverityReadonly43["ECK - Coverity - Readonly"]:::product
    AAPlatformECKCoverityAdmin([AAPlatform - ECK - Coverity - Admin]):::category --> ECKCoverityAdmin44["ECK - Coverity - Admin"]:::product
    MSOLLicenseMicrosoftPowerBIReadOnlyAccess([MSOL License - Microsoft Power BI (Read-Only Access)]):::category --> PowerBICoverity46["Power BI- Coverity"]:::product
    ITDevOpsAutomationTeamAdminonAZADCORP([IT DevOps Automation Team Admin on AZAD-CORP]):::category --> RunningDunctionaltestsuiteinGI48["Running Dunctional test suite in GITHUB-Coverity"]:::product
```
