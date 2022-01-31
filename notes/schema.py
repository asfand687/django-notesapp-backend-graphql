import graphene
from graphene_django import DjangoObjectType
from .models import Note
from django.contrib.auth import get_user_model


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = ("id", "body", "created", "owner")


class Query(graphene.ObjectType):
    all_notes = graphene.List(NoteType)

    def resolve_all_notes(root, info):
        return Note.objects.all()


class CreateNote(graphene.Mutation):
    note = graphene.Field(NoteType)

    class Arguments:
        body = graphene.String(required=True)
        ownerId = graphene.ID()

    def mutate(self, info, body, ownerId):
        note = Note(body=body, owner_id=ownerId)
        note.save()
        return CreateNote(
            note
        )


class UpdateNote(graphene.Mutation):
    note = graphene.Field(NoteType)

    class Arguments:
        id = graphene.ID()
        body = graphene.String(required=True)

    def mutate(self, info, id, body):
        note = Note.objects.get(id=id)
        note.body = body
        note.save()

        return UpdateNote(
            note
        )


class DeleteNote(graphene.Mutation):
    msg = graphene.String()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        note = Note.objects.get(id=id)
        note.delete()
        return DeleteNote(
            msg="note deleted successfull"
        )


class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()
    update_note = UpdateNote.Field()
    delete_note = DeleteNote.Field()
