Name:		osgi-core
Version:	6.0.0
Release:	5.1
Summary:	OSGi Core API
Group:		Development/Java
License:	ASL 2.0
URL:		https://www.osgi.org/
Source0:	https://repo1.maven.org/maven2/org/osgi/osgi.core/%{version}/osgi.core-%{version}-sources.jar
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	mvn(org.osgi:org.osgi.annotation.versioning)
BuildSystem:	maven
BuildOption(install):	--file-name %{name} --alias org.osgi:org.osgi.core

%description
OSGi Core Release 6 interfaces and classes for compiling bundles.

%prep
%setup -q -c -T
# The builders' rpmuncompress passes a sources jar to tar.
python - %{SOURCE0} <<'PY'
import sys
import zipfile
zipfile.ZipFile(sys.argv[1]).extractall(".")
PY
mkdir -p src/main/java
mv org src/main/java/
python - %{version} <<'PY'
import sys
from pathlib import Path
version = sys.argv[1]
Path("pom.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.osgi</groupId>
  <artifactId>osgi.core</artifactId>
  <version>{version}</version>
  <packaging>jar</packaging>
  <name>OSGi Core</name>
  <dependencies>
    <dependency>
      <groupId>org.osgi</groupId>
      <artifactId>org.osgi.annotation.versioning</artifactId>
      <scope>provided</scope>
    </dependency>
  </dependencies>
</project>
""")
PY

%files -f .mfiles
%doc LICENSE about.html
