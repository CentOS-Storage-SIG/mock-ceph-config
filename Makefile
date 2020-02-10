NAME = mock-ceph-config

ifndef DISTRO
  $(error DISTRO is undefined, set to "el7")
endif


DIST := ".${DISTRO}"

VERSION := $(shell rpmspec \
             --define "dist ${DIST}" \
             -q --srpm --qf "%{version}\n" ${NAME}.spec)

RELEASE := $(shell rpmspec \
             --define "dist ${DIST}" \
             -q --srpm --qf "%{release}\n" ${NAME}.spec)

NVR := ${NAME}-${VERSION}-${RELEASE}
SRPM := ${NVR}.src.rpm

all: srpm

srpm: $(SRPM)

$(SRPM):
	rpmbuild -bs \
		--define "_sourcedir ." --define "_srcrpmdir ." \
		--define "dist $(DIST)" \
		$(NAME).spec

build: $(SRPM)
	ifeq ($(DISTRO),el8)
		# XXX: remove hard-coded "8" here:
		cbs build storage8-ceph-nautilus-$(DISTRO) $(SRPM) && \
		cbs tag-build storage8-ceph-nautilus-testing $(NVR)
	else
		# XXX: remove hard-coded "7" here:
		cbs build storage7-ceph-luminous-$(DISTRO) $(SRPM) && \
		cbs tag-build storage7-ceph-luminous-testing $(NVR) && \
		cbs tag-build storage7-ceph-nautilus-candidate $(NVR) && \
		cbs tag-build storage7-ceph-nautilus-testing $(NVR)
	endif

.PHONY: all build srpm
