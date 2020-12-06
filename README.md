kube-container-status-exporter
------------------------------

Controllers managed pods when container status changes get lost as soon as containers are restarted. This exporter will log/export (planned) state changes.

#### Implementation
Stream container state changes to stdout. Banzai Cloud Logging pipeline will pick up from there to configured `ClusterFlow` or `Flow`.

#### Image Repository:
https://gallery.ecr.aws/a4i9p0w5/moengage/kube-container-status-exporter

#### Installations:
By default it installs in `kube-system` namespace, feel free to change it any other namespace, change ClusterRolebinding accordingly.

```bash
$ git clone https://github.com/moengage/kube-container-status-exporter/
$ cd deployments
$ kubectl apply -f .
$ stern kube-container-status-exporter/w+ -n kube-system
```
