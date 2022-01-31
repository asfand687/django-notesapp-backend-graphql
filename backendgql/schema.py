import graphene
import notes.schema
import accounts.schema


class Query(notes.schema.Query, accounts.schema.Query, graphene.ObjectType):
    pass


class Mutation(notes.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
