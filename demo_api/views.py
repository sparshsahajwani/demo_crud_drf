from rest_framework.response import Response
from product.models import Product,Compnay
from product.serializers import ProductSerializer, CompanySerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
# from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import BasicAuthentication
# from rest_framework import generics
# from rest_framework.renderers import TemplateHTMLRenderer


# class TemplateResponseCheck(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
    
#     def get(self, request, *args, **kwargs):
#         product = get_object_or_404(Product, pk=kwargs['pk']) 
#         return Response({'product': product}, template_name='product.html')
    
class CompanyList(APIView):
    def get(self , request):
        company = Compnay.objects.all()
        companySerializer = CompanySerializer(company,many=True)
        return Response(companySerializer.data)
    def post(self , request):
        postCompanySerializer = CompanySerializer(data=request.data)
        if postCompanySerializer.is_valid():
            postCompanySerializer.save()
            return Response(postCompanySerializer.data)     
        return Response(postCompanySerializer.errors)

class CompanyDetail(APIView):
    def get_object(self,id):
        try:
            return Compnay.objects.get(id=id)
        except Compnay.DoesNotExist:
            return Http404
    
    def get(self,request,id):
        company = self.get_object(id)
        companySerializer = CompanySerializer(company)
        return Response(companySerializer.data)
    
    def put(self, request, id):
        company = self.get_object(id)
        postCompanySerailizer = CompanySerializer(company,data=request.data ,partial=True)
        if postCompanySerailizer.is_valid():
            postCompanySerailizer.save()
            return Response(postCompanySerailizer.data)
        return Response(postCompanySerailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delele(self, request,id):
        company = self.get_object(id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductList(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self , request):
        product = Product.objects.all()
        productSerializer = ProductSerializer(product,many=True)
        return Response(productSerializer.data)
    def post(self , request):
        postProductSerializer = ProductSerializer(data=request.data)
        if postProductSerializer.is_valid():
            postProductSerializer.save()
            return Response(postProductSerializer.data)     
        return Response(postProductSerializer.errors)

class ProductDetail(APIView):

    def get_object(self,id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Http404
    
    def get(self,request,id):
        product = self.get_object(id)
        productSerializer = ProductSerializer(product)
        return Response(productSerializer.data)
    
    def put(self, request, id):
        product = self.get_object(id)
        postProductSerailizer = ProductSerializer(product,data=request.data ,partial=True)
        if postProductSerailizer.is_valid():
            postProductSerailizer.save()
            return Response(postProductSerailizer.data)
        return Response(postProductSerailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delele(self, request,id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

