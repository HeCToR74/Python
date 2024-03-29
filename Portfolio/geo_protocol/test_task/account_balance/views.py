from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Action, Balance
from .serializers import ActionSerializer, CustomerSerializer, BalanceSerializer

def save_action(action, customer_id):
    saved_customer = get_object_or_404(Customer.objects.all(), pk=customer_id)
    data = {"name": saved_customer.name, "balance":
        saved_customer.balance + action["point"] if saved_customer.balance + action["point"] >= 0 else 0}
    serializer_customer = CustomerSerializer(instance=saved_customer, data=data, partial=True)
    if serializer_customer.is_valid(raise_exception=True):
        customer_saved = serializer_customer.save()

class ActionView(APIView):
    def get(self, request):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response({"actions": serializer.data})

    def post(self, request):
        action = request.data.get('action')
        serializer_action = ActionSerializer(data=action)
        if serializer_action.is_valid(raise_exception=True):
            action_saved = serializer_action.save()
            save_action(action, action_saved.name.id)
        return Response({"success": "Action created successfully"})

class CustomerView(APIView):
    def get(self, request):
        customeres = Customer.objects.all()
        serializer = CustomerSerializer(customeres, many=True)
        return Response({"customeres": serializer.data})

class CustomerViewId(APIView):
    def get(self, request, pk):
        customer =  get_object_or_404(Customer.objects.all(), pk=pk)
        actions = Action.objects.filter(name=customer.id)
        serializer = ActionSerializer(actions, many=True)
        list_actions = [{"point": item["point"],
                         "description": item["description"],
                         "date": item["date"],
                         } for item in serializer.data]
        return Response({customer.name + ', balance: ' + str(customer.balance): list_actions})

    def post(self, request, pk):
        request_data = request.data.get('action')
        action = {"point": request_data["point"],
                  "description": request_data["description"],
                  "date": request_data["date"],
                  "name_id": pk
                  }
        serializer_action = ActionSerializer(data=action)
        if serializer_action.is_valid(raise_exception=True):
            action_saved = serializer_action.save()
            save_action(action, pk)
        return Response({"success": "Action created successfully"})

class BalanceView(APIView):
    def post(self, request):
        balance_record = request.data.get('balance')
        serializer_balance_record = BalanceSerializer(data=balance_record)
        if serializer_balance_record.is_valid(raise_exception=True):
            balance_record_saved = serializer_balance_record.save()
        return Response({"success": "Balance record created successfully"})