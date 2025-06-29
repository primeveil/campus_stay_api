from rest_framework import serializers
from reviews.models import PropertyReview

class PropertyReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.SerializerMethodField()
    
    class Meta:
        model = PropertyReview
        fields = ['id', 'property', 'reviewer', 'reviewer_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['reviewer', 'created_at']
    
    def get_reviewer_name(self, obj):
        return f"{obj.reviewer.first_name} {obj.reviewer.last_name}"

