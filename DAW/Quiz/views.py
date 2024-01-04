from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['GET'])
def get_quizs(request):
    questionnaires = Questionnaire.objects.all()
    serializers = QuestionnaireSerializer(questionnaires, many=True)
    return Response(
        {
            'Quizs': serializers.data
        }
    )



@api_view(['GET'])
def get_response_quizs(request):
    response_questionnaires = ResponsesQuestionnaire.objects.all()
    serializers = ReponseQuestionnaireSerializer(response_questionnaires, many=True)
    return Response(
        {
            'response_questionnaires': serializers.data
        }
    )


# Create your views here.



@api_view(['POST'])
# @login_required
def response_quiz(request):
    data = request.data
    response_q = ReponseQuestionnaireSerializer(data=data)
    # paitent = get_object_or_404(Patient,idUser=request.user)
    # data['id_Patient']=paitent.id
    if response_q.is_valid():
        
        validated_data = response_q.validated_data
        if not ResponsesQuestionnaire.objects.filter(id_Questionnaire=validated_data['id_Questionnaire'],id_Patient=validated_data['id_Patient']).exists() :

            data = ResponsesQuestionnaire.objects.create(
            id_Patient = validated_data['id_Patient'],
            id_Questionnaire = validated_data['id_Questionnaire']
            )
            return Response({
                "details":"Response is created successfully!",
            },status=status.HTTP_201_CREATED)
        else : 
            return Response({
                "details":"You already respose for this quiz!",
            },status=status.HTTP_400_BAD_REQUEST)
    else :
        return Response(response_q.errors)


# @api_view(['POST'])
# # @login_required
# def response_question(request):
#     data = request.data
#     response_q = ResponsesQuestionSerializer(data=data)
#     if response_q.is_valid():
#         validated_data = response_q.validated_data
#         data = ResponsesQuestion.objects.create(
#         id_Reponse_Questionnaire = validated_data['id_Reponse_Questionnaire'],
#         id_Option = validated_data['id_Option']
#         )
#         reponse_quiz = get_object_or_404(ResponsesQuestionnaire,id = validated_data['id_Reponse_Questionnaire'])
#         option = get_object_or_404(Option, id=validated_data['id_Option'])
#         reponse_quiz.score += float(option.point)
#         reponse_quiz.save()
#         return Response({
#             "details":"Response is created successfully!",
#         },status=status.HTTP_201_CREATED)
#     else :
#         return Response(response_q.errors)


@api_view(['POST'])
def response_question(request):
    data = request.data
    response_q = ResponsesQuestionSerializer(data=data)
    
    if response_q.is_valid():
        validated_data = response_q.validated_data
        data = ResponsesQuestion.objects.create(
            id_Reponse_Questionnaire = validated_data['id_Reponse_Questionnaire'],
            id_Option = validated_data['id_Option']
        )
        # Assuming id_Option is an ID, not an object
        # option_id = validated_data['id_Option']
        # # option = get_object_or_404(Option,id=option_id)
        # option = Option.objects.get_or_create(id='id_Option')
        # reponse_quiz = get_object_or_404(ResponsesQuestionnaire,id=validated_data['id_Reponse_Questionnaire'])
        # reponse_quiz.score += float(option.point)
        # reponse_quiz.save()
        
        return Response({
            "details": "Response is created successfully!",
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(response_q.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def register(request):
#     data = request.data
#     user = SignUpSerializer(data=data)
#     if user.is_valid() : 
#         if not User.objects.filter(username = data['email']).exists():
#             user = User.objects.create(  
#                 first_name = data['first_name'],
#                 last_name = data['last_name'],
#                 email = data['email'],
#                 password = make_password(data['password']),
#                 username = data['email'],
#             )

#             return Response({
#                 'details':'Your account registred successfully',
#             },status=status.HTTP_201_CREATED)
        
#         else :
#             return Response({
#                     'details':'This email already exists'
#             },status=status.HTTP_400_BAD_REQUEST)
    
#     else : 
#         return Response(user.errors)
    