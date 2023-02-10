# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osv_service_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from osv import vulnerability_pb2 as osv_dot_vulnerability__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14osv_service_v1.proto\x12\x06osv.v1\x1a\x17osv/vulnerability.proto\x1a\x1cgoogle/api/annotations.proto\"O\n\x11VulnerabilityList\x12!\n\x05vulns\x18\x01 \x03(\x0b\x32\x12.osv.Vulnerability\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"D\n\x16\x42\x61tchVulnerabilityList\x12*\n\x07results\x18\x01 \x03(\x0b\x32\x19.osv.v1.VulnerabilityList\"h\n\x05Query\x12\x10\n\x06\x63ommit\x18\x01 \x01(\tH\x00\x12\x11\n\x07version\x18\x02 \x01(\tH\x00\x12\x1d\n\x07package\x18\x04 \x01(\x0b\x32\x0c.osv.Package\x12\x12\n\npage_token\x18\x05 \x01(\tB\x07\n\x05param\",\n\nBatchQuery\x12\x1e\n\x07queries\x18\x01 \x03(\x0b\x32\r.osv.v1.Query\"#\n\x15GetVulnByIdParameters\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\x17QueryAffectedParameters\x12\x1c\n\x05query\x18\x01 \x01(\x0b\x32\r.osv.v1.Query\"A\n\x1cQueryAffectedBatchParameters\x12!\n\x05query\x18\x01 \x01(\x0b\x32\x12.osv.v1.BatchQuery\"A\n\x1a\x44\x65termineVersionParameters\x12#\n\x05query\x18\x01 \x01(\x0b\x32\x14.osv.v1.VersionQuery\"C\n\x0cVersionQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x0b\x66ile_hashes\x18\x02 \x03(\x0b\x32\x10.osv.v1.FileHash\">\n\x08\x46ileHash\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x11\n\thash_type\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\"9\n\x10VersionMatchList\x12%\n\x07matches\x18\x01 \x03(\x0b\x32\x14.osv.v1.VersionMatch\"\xd7\x01\n\x0cVersionMatch\x12\r\n\x05score\x18\x01 \x01(\x01\x12\x37\n\trepo_info\x18\x02 \x01(\x0b\x32$.osv.v1.VersionRepositoryInformation\x12$\n\x0eosv_identifier\x18\x03 \x01(\x0b\x32\x0c.osv.Package\x12,\n\x04\x63pes\x18\x04 \x03(\x0b\x32\x1e.osv.v1.VersionMatch.CpesEntry\x1a+\n\tCpesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc0\x01\n\x1cVersionRepositoryInformation\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.osv.v1.VersionRepositoryInformation.RepoType\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06\x63ommit\x18\x03 \x01(\x0c\x12\x0b\n\x03tag\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"$\n\x08RepoType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x07\n\x03GIT\x10\x01\x32\xc5\x03\n\x03OSV\x12X\n\x0bGetVulnById\x12\x1d.osv.v1.GetVulnByIdParameters\x1a\x12.osv.Vulnerability\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/vulns/{id}\x12\x65\n\rQueryAffected\x12\x1f.osv.v1.QueryAffectedParameters\x1a\x19.osv.v1.VulnerabilityList\"\x18\x82\xd3\xe4\x93\x02\x12\"\t/v1/query:\x05query\x12y\n\x12QueryAffectedBatch\x12$.osv.v1.QueryAffectedBatchParameters\x1a\x1e.osv.v1.BatchVulnerabilityList\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x0e/v1/querybatch:\x05query\x12\x81\x01\n\x10\x44\x65termineVersion\x12\".osv.v1.DetermineVersionParameters\x1a\x18.osv.v1.VersionMatchList\"/\x82\xd3\xe4\x93\x02)\" /v1experimental/determineversion:\x05queryb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osv_service_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VERSIONMATCH_CPESENTRY._options = None
  _VERSIONMATCH_CPESENTRY._serialized_options = b'8\001'
  _OSV.methods_by_name['GetVulnById']._options = None
  _OSV.methods_by_name['GetVulnById']._serialized_options = b'\202\323\344\223\002\020\022\016/v1/vulns/{id}'
  _OSV.methods_by_name['QueryAffected']._options = None
  _OSV.methods_by_name['QueryAffected']._serialized_options = b'\202\323\344\223\002\022\"\t/v1/query:\005query'
  _OSV.methods_by_name['QueryAffectedBatch']._options = None
  _OSV.methods_by_name['QueryAffectedBatch']._serialized_options = b'\202\323\344\223\002\027\"\016/v1/querybatch:\005query'
  _OSV.methods_by_name['DetermineVersion']._options = None
  _OSV.methods_by_name['DetermineVersion']._serialized_options = b'\202\323\344\223\002)\" /v1experimental/determineversion:\005query'
  _VULNERABILITYLIST._serialized_start=87
  _VULNERABILITYLIST._serialized_end=166
  _BATCHVULNERABILITYLIST._serialized_start=168
  _BATCHVULNERABILITYLIST._serialized_end=236
  _QUERY._serialized_start=238
  _QUERY._serialized_end=342
  _BATCHQUERY._serialized_start=344
  _BATCHQUERY._serialized_end=388
  _GETVULNBYIDPARAMETERS._serialized_start=390
  _GETVULNBYIDPARAMETERS._serialized_end=425
  _QUERYAFFECTEDPARAMETERS._serialized_start=427
  _QUERYAFFECTEDPARAMETERS._serialized_end=482
  _QUERYAFFECTEDBATCHPARAMETERS._serialized_start=484
  _QUERYAFFECTEDBATCHPARAMETERS._serialized_end=549
  _DETERMINEVERSIONPARAMETERS._serialized_start=551
  _DETERMINEVERSIONPARAMETERS._serialized_end=616
  _VERSIONQUERY._serialized_start=618
  _VERSIONQUERY._serialized_end=685
  _FILEHASH._serialized_start=687
  _FILEHASH._serialized_end=749
  _VERSIONMATCHLIST._serialized_start=751
  _VERSIONMATCHLIST._serialized_end=808
  _VERSIONMATCH._serialized_start=811
  _VERSIONMATCH._serialized_end=1026
  _VERSIONMATCH_CPESENTRY._serialized_start=983
  _VERSIONMATCH_CPESENTRY._serialized_end=1026
  _VERSIONREPOSITORYINFORMATION._serialized_start=1029
  _VERSIONREPOSITORYINFORMATION._serialized_end=1221
  _VERSIONREPOSITORYINFORMATION_REPOTYPE._serialized_start=1185
  _VERSIONREPOSITORYINFORMATION_REPOTYPE._serialized_end=1221
  _OSV._serialized_start=1224
  _OSV._serialized_end=1677
# @@protoc_insertion_point(module_scope)
