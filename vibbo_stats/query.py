vibboThreadsQuery = """
query vibboThreadsQuery(
    $organizationId: OrganizationID!,
    $boardPerspective: Boolean!,
    $status: ThreadStatus!,
    $correspondentUserId: NodeID,
    $assigneeUserId: NodeID,
    $apartmentNumber: Int,
    $topicId: NodeID,
    $search: String,
    $limit: Int!,
    $afterDate: DateTime
) {
    organization(id: $organizationId) {
        id
        threads(
            filters: {
                search: $search,
                status: $status,
                correspondentUserId: $correspondentUserId,
                assigneeUserId: $assigneeUserId,
                apartmentNumber: $apartmentNumber,
                topicId: $topicId,
                boardPerspective: $boardPerspective
            }
            limit: $limit
            afterDate: $afterDate
        ) {
            threads {
                id
                slug
                title
                lastMessageAt
                topic {
                    id
                    slug
                    title
                }
                messages {
                    id
                    body
                    createdBy {
                        id
                        userId
                        name
                    }
                }
            }
        }
    }
}
"""