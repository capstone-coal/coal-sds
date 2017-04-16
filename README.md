# coal-sds

An [Apache OODT](http://oodt.apache.org)-powered Science Data System (SDS) for [COAL](https://github.com/capstone-coal).

# Introduction
coal-sds is an end-to-end SDS capable of managing the data lifecycle 
(aquisition, cataloging, archival, retrieval, processing, etc.) required for COAL.
The [Apache OODT](http://oodt.apache.org)-poweredSDS itself consists of 
several components which when run as services, allow users to really explore COAL in its entirety.

# Requirements
* Java Development Kit (JDK) 1.8+
* JAVA_HOME set 

# Installation

## Build OODT
```
$ mvn clean package <OPTIONAL PROFILES> # see optional build profiles below
```
Typically efficient and effective cataloguing is achieved by passing the ```-Pfm-solr-catalog``` option 
as this allows all data flowing into the SDS to be persisted into [Apache Solr](http://lucene.apache.org/solr).

## Deploy OODT
```  
$ tar zxf distribution/target/${PROJECT_ARTIFACT_ID}-distribution-*-bin.tar.gz -C /my/deployment/directory/oodt
```  
  ---
  NOTE: For other build configurations, add the following arguments:
  (default)           : bin, crawler, data, extensions,
                        filemgr (Lucene), logs, pcs, resmgr,
                        tomcat, workflow, pge

  -Pfm-solr-catalog   : default components, filemgr (Solr),
                        solr, tomcat/webapps/solr

# Running
See [Running COAL SDS](https://github.com/capstone-coal/coal-sds/wiki/Running-COAL-SDS)

# License
coal-sds is licensed permissively under the [Apache License v2.0](https://www.apache.org/licenses/LICENSE-2.0) 
a copy of which ships with this code.
