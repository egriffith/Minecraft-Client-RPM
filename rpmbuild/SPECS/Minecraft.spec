Name:		Minecraft
Version:	1.6.11
Release:	1%{?dist}
Summary:	Sandbox adventure game by Mojang AB

License:	Mojang Minecraft EULA
URL:		https://minecraft.net/
Source0:	https://s3.amazonaws.com/Minecraft.Download/launcher/Minecraft.jar
Source1:	Minecraft/minecraft
Source2:	Minecraft/minecraft.png
Source3:	Minecraft/minecraft.desktop
Source4:	Minecraft/LICENSE
BuildArch:	noarch

BuildRequires:	java,desktop-file-utils
Requires:	java 

%description 
"Java based Sandbox adventure game written by Mojang AB."


%prep


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_prefix}/share/Mojang/Minecraft/
mkdir -p %{buildroot}%{_prefix}/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}%{_prefix}/share/applications/
mkdir -p %{buildroot}%{_prefix}/share/licenses/Mojang/Minecraft

cp -p %SOURCE0 %{buildroot}%{_prefix}/share/Mojang/Minecraft/
cp -p %SOURCE1 %{buildroot}%{_bindir}/
cp -p %SOURCE2 %{buildroot}%{_prefix}/share/icons/hicolor/256x256/apps/
desktop-file-install --dir=%{buildroot}%{_datadir}/share/applications/ %SOURCE3
cp -p %SOURCE4 %{buildroot}%{_prefix}/share/licenses/Mojang/Minecraft/

%files
%{_bindir}/minecraft
%{_prefix}/share/Mojang/Minecraft/Minecraft.jar
%{_prefix}/share/icons/hicolor/256x256/apps/minecraft.png
%{_prefix}/share/applications/minecraft.desktop
%{_prefix}/share/licenses/Mojang/Minecraft/



%changelog
* Mon Mar  2 2015 Eric Griffith
- 
