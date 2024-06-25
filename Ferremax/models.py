from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True)
    nombreTipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombreTipoUsuario)


class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreCategoria)


class marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    nombreMarca = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreMarca)


class proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    nombreProveedor = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreProveedor)


class cargo(models.Model):
    idCargo= models.AutoField(primary_key=True)
    nombreCargo = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreCargo)


class producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=20, blank=False, null=False)
    stockProducto = models.IntegerField()
    descripcionProducto = models.CharField(max_length=100, blank=False, null=False)
    precioProducto = models.IntegerField()
    imagenProducto = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey("categoria", on_delete=models.CASCADE)
    marca = models.ForeignKey("marca", on_delete=models.CASCADE)
    proveedor = models.ForeignKey("proveedor", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreProducto)


class empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombreEmpleado = models.CharField(max_length=20, blank=False, null=False)
    nombreCompleto = models.CharField(max_length=20, blank=False, null=False)
    correo = models.CharField(max_length=20, blank=False, null=False)
    edad = models.IntegerField()
    contraseña = models.CharField(max_length=20, blank=False, null=False)
    cargo = models.ForeignKey("cargo", on_delete=models.CASCADE)
    tipoUsuario = models.ForeignKey("tipoUsuario", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreCompleto)


class usuario(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=20, blank=False, null=False)
    nombreCompleto = models.CharField(max_length=20, blank=False, null=False)
    correo = models.CharField(max_length=20, blank=False, null=False)
    contraseña = models.CharField(max_length=20, blank=False, null=False)
    tipoUsuario = models.ForeignKey("tipoUsuario", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreCompleto)


class pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    idOrden = models.IntegerField()
    idSesion = models.IntegerField()
    direccionPedido = models.CharField(max_length=50, blank=False, null=False)
    fechaPedido = models.DateField(blank=False, null=False)
    totalPedido = models.IntegerField()
    usuario = models.ForeignKey("usuario", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idPedido)+" "+str(self.usuario)


class detallePedido(models.Model):
    pedido = models.ForeignKey("pedido", on_delete=models.CASCADE)
    producto = models.ForeignKey("producto", on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField()
    subtotalPedido = models.IntegerField()

    def __str__(self):
        return str(self.pedido)+" "+str(self.producto)