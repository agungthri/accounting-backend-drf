from rest_framework import serializers
from app.models import Account, Transaction, Journal


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'account', 'amount', 'position', 'amount']
        read_only_fields = ['id']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
        depth = 2


class TransactionJournalSerializer(serializers.ModelSerializer):
    journal_transaction = JournalSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['id', "journal_transaction", 'date', 'type', 'desc']
        read_only_fields = ['id']

    def create(self, validated_data):
        journal_transaction_data = validated_data.pop('journal_transaction')
        transaction = Transaction.objects.create(**validated_data)
        for data in journal_transaction_data:
            Journal.objects.create(transaction=transaction, **data)
        return transaction








