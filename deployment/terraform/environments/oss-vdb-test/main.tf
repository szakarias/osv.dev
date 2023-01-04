module "osv_test" {
  source = "../../modules/osv"

  project_id = "oss-vdb-test"

  public_import_logs_bucket     = "osv-test-public-import-logs"
  vulnerabilities_export_bucket = "osv-test-vulnerabilities"
}


terraform {
  backend "gcs" {
    bucket = "oss-vdb-tf"
    prefix = "oss-vdb-test"
  }
}
