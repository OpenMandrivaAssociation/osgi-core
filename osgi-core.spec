%{?_javapackages_macros:%_javapackages_macros}

Name:           osgi-core
Version:        6.0.0
Release:        5.1
License:        ASL 2.0
Group:          Development/Java
Summary:        OSGi Core API
URL:            https://www.osgi.org
Source0:        https://repo1.maven.org/maven2/org/osgi/osgi.core/%{version}/osgi.core-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/org/osgi/osgi.core/%{version}/osgi.core-%{version}.pom
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.annotation)


%description
OSGi Core Release 6, Interfaces and Classes for use in compiling bundles.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
%setup -q -c

cp -p %SOURCE1 pom.xml
mkdir -p src/main/java
mv org src/main/java/

%pom_xpath_inject pom:project '
<packaging>bundle</packaging>
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-Name>${project.artifactId}</Bundle-Name>
          <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>'

%pom_add_dep org.osgi:osgi.annotation::provided

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 6.0.0-3
- Fix scopes of injected Maven dependencies

* Wed Oct 05 2016 Michael Simacek <msimacek@redhat.com> - 6.0.0-2
- Remove alias

* Tue Oct 04 2016 Michael Simacek <msimacek@redhat.com> - 6.0.0-1
- Initial packaging

