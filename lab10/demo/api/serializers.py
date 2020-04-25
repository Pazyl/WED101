
from rest_framework import serializers

from .models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=300, default='', allow_blank=True)
    city = serializers.CharField(required=True, max_length=50)
    address = serializers.CharField(required=False, max_length=300, default='', allow_blank=True)

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company
        # company = Company.objects.create(name=validated_data.get('name'))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=300, default='')
    city = serializers.CharField(required=True, max_length=50)
    address = serializers.CharField(required=False, max_length=300, default='')

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')
        # fields = '__all__'


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=300, default='')
    salary = serializers.FloatField(required=True)
    company = CompanySerializer(read_only=True)


class VacancySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=300, default='', allow_blank=True)
    salary = serializers.FloatField(required=True)
    company = CompanySerializer2(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company', 'company_id')
        # fields = '__all__'
