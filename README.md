# devops-netology

Из-за правил в terraform/.gitignore в папке terraform будут игнорироваться:

- все файлы в поддиректории .terraform;
- все файлы имеющие расширение \*.tfstate, а также \*.tfstate.\*;
- все файлы с именем crash.log, а также производными crash.*.log;
- все файлы с расширением *.tfvars и *.tfvars.json;
- файлы имеющие имена override.tf и override.tf.json;
- все файлы имена (с расширениями \*.tf и *.tf.json) которых заканчиваются на \*_override.tf
\*_override.tf.json;
- а также файлы имеющие имена .terraformrc и terraform.rc.
