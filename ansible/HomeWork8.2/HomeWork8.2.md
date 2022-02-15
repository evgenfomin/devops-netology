1 \
Подготовил инвентори файл: 
```
---
elasticsearch:
  hosts:
    elastic:
      ansible_connection: docker
      ansible_user: root
kibana:
  hosts:
    kibana:
      ansible_connection: docker
      ansible_user: root
```
2 \
Дописал playbook для kibana \
```
- name: Install Kibana
  hosts: kibana
  tasks:
    - name: Upload tar.gz Elasticsearch from remote URL
      get_url:
        url: "https://artifacts.elastic.co/downloads/kibana/kibana-{{ ribana_version }}-linux-x86_64.tar.gz"
        dest: "/tmp/elasticsearch-{{ kibana_version }}-linux-x86_64.tar.gz"
        mode: 0755
        timeout: 60
        force: true
        validate_certs: false
      register: get_kibana
      until: get_kibana is succeeded
      tags: kibana
    - name: Create directrory for Kibana
      file:
        state: directory
        path: "{{ kibana_home }}"
      tags: kibana
    - name: Extract Kibana in the installation directory
      become: true
      unarchive:
        copy: false
        src: "/tmp/kibana-{{ kibana_version }}-linux-x86_64.tar.gz"
        dest: "{{ kibana_home }}"
        extra_opts: [--strip-components=1]
        creates: "{{ kibana_home }}/bin/elasticsearch"
      tags:
        - kibana
    - name: Set environment kibana
      become: true
      template:
        src: templates/kibana.sh.j2
        dest: /etc/profile.d/kibana.sh
      tags: kibana
```
3 \ 
ready \
4 \
ready \
5 \
Запустил ansible-lint site.yml
```
Finished with 0 failure(s), 7 warning(s) on 1 files.
```
6 \
при запуске с флагом --check отваливается с ошибкой т.к не были скачены архивы для elfstic and kibana \

7 \
запустил изменения все прошли \

8 \
```
PLAY RECAP ********************************************************************************************************************************************************************
elastic                    : ok=9    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana                     : ok=10   changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```
