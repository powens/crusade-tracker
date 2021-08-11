from django.db import models
from django.contrib.auth.models import User


class PointsPlChoices(models.TextChoices):
    POINTS = "POINTS", "Points"
    PL = "PL", "PL"


class RoleChoices(models.TextChoices):
    HQ = "HQ", "HQ"
    TROOPS = "TROOPS", "Troops"
    ELITE = "ELITE", "Elite"
    FA = "FA", "Fast Attack"
    FLYER = "FLYER", "Flyer"
    HS = "HS", "Heavy Support"
    FORTIFICATION = "FORTIFICATION", "Fortification"
    LOW = "LOW", "Lord of War"
    DT = "DT", "Dedicated Transport"
    NS = "NS", "No Slot"


class OrderOfBattle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    faction = models.CharField(max_length=64)
    player_name = models.CharField(max_length=64)
    description = models.TextField()
    rp = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    points_or_pl = models.TextField(
        max_length=6,
        choices=PointsPlChoices.choices,
        default=PointsPlChoices.PL,
    )


class Unit(models.Model):
    oob = models.ForeignKey(OrderOfBattle, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    datasheet_name = models.CharField(max_length=128)
    datasheet_source = models.CharField(max_length=64)
    role = models.CharField(
        max_length=16,
        choices=RoleChoices.choices,
        default=RoleChoices.HQ,
    )
    points = models.IntegerField()
    model_count = models.IntegerField()
    is_character = models.BooleanField()
    is_psyker = models.BooleanField()
    is_battle_ready = models.BooleanField()
    is_exp_ineligible = models.BooleanField()
    description = models.TextField()
    other_rules = models.TextField()
    exp_adjustment = models.IntegerField()
    cp_adjustment = models.IntegerField()


class UnitUpgrade(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField()
