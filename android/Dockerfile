FROM hivesolutions/alpine_dev:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ENV JAVA_VERSION="8"\
    JAVA_UPDATE="271"\
    JAVA_HOME="/usr/lib/jvm/default-jvm"\
    GLIBC_REPO="https://github.com/sgerrand/alpine-pkg-glibc"\
    GLIBC_VERSION="2.29-r0"

RUN apk upgrade --update

RUN apk add --no-cache --virtual=build-jre wget unzip &&\
    cd "/tmp" &&\
    apk add libstdc++ ca-certificates java-cacerts bash &&\
    wget --no-verbose "${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" &&\
    wget --no-verbose "${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" &&\
    wget --no-verbose "${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk" &&\
    apk add --allow-untrusted /tmp/*.apk &&\
    (/usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 || true) &&\
    echo "export LANG=en_US.UTF-8" > /etc/profile.d/locale.sh &&\
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib &&\
    wget --no-verbose --header "Cookie: oraclelicense=accept-securebackup-cookie;"\
        "https://archive.hive.pt/files/jdk/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" &&\
    tar -xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" &&\
    mkdir -p "/usr/lib/jvm" &&\
    mv "/tmp/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}" "/usr/lib/jvm/java-${JAVA_VERSION}" &&\
    ln -s "java-${JAVA_VERSION}" "$JAVA_HOME" &&\
    ln -s "$JAVA_HOME/bin/"* "/usr/bin/" &&\
    ln -sf "/etc/ssl/certs/java/cacerts" "$JAVA_HOME/jre/lib/security/cacerts" &&\
    apk del build-jre &&\
    rm -r "/tmp/"*

ENV ANDROID_SDK_HOME="/opt/android-sdk-linux"\
    ANDROID_SDK_ROOT="/opt/android-sdk-linux"\
    ANDROID_HOME="/opt/android-sdk-linux"\
    ANDROID_SDK="/opt/android-sdk-linux"\
    ANDROID_SDK_TOOLS_VERSION="4333796"

RUN [ -d $ANDROID_SDK_HOME ] || mkdir -p "$ANDROID_SDK_HOME" &&\
    [ -d $ANDROID_SDK_ROOT ] || mkdir -p "$ANDROID_SDK_ROOT" &&\
    [ -d $ANDROID_HOME ]  || mkdir -p "$ANDROID_HOME" &&\
    [ -d $ANDROID_SDK ] || mkdir -p "$ANDROID_SDK"

RUN apk add --no-cache --virtual=build-android wget unzip &&\
    cd "/tmp" &&\
    wget --no-verbose "https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip" &&\
    unzip -q "sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip" -d "$ANDROID_SDK_HOME" &&\
    mkdir -p "$ANDROID_SDK_HOME/licenses" &&\
    echo "24333f8a63b6825ea9c5514f83c2829b004d1fee" > "$ANDROID_SDK_HOME/licenses/android-sdk-license" &&\
    echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> "$ANDROID_SDK_HOME/licenses/android-sdk-license" &&\
    mkdir -p "$ANDROID_SDK_HOME/.android" && touch "$ANDROID_SDK_HOME/.android/repositories.cfg" &&\
    $ANDROID_SDK_HOME/tools/bin/sdkmanager --update &&\
    ANDROID_BUILD_TOOLS_LATEST=$($ANDROID_SDK_HOME/tools/bin/sdkmanager --list --channel=0 | grep "build-tools" |\
        cut -d "|" -f 1 | tr -d " " | sort -t ";" -r -g -k2 | head -n1) &&\
    ANDROID_LATEST=$($ANDROID_SDK_HOME/tools/bin/sdkmanager --list --channel=0 | grep "platforms;android-" |\
        cut -d "|" -f 1 | tr -d " " | sort -t "-" -r -g -k2 | head -n1) &&\
    yes | $ANDROID_SDK_HOME/tools/bin/sdkmanager "platform-tools" "${ANDROID_BUILD_TOOLS_LATEST}" "${ANDROID_LATEST}" &&\
    apk del build-android &&\
    rm -r "/tmp/"*

ENV GRADLE_HOME="/usr/lib/gradle"\
    GRADLE_VERSION="6.7.1"

RUN apk add --no-cache --virtual=build-gradle wget unzip &&\
    cd "/tmp" &&\
    wget --no-verbose "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" &&\
    unzip -q "gradle-${GRADLE_VERSION}-bin.zip" &&\
    mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" &&\
    ln -s "${GRADLE_HOME}/bin/gradle" "/usr/bin/gradle" &&\
    apk del build-gradle &&\
    rm -r "/tmp/"*
