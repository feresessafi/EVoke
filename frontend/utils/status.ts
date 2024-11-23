export const getStatusVariant = (status: string) => {
  switch (status) {
    case 'Review Needed':
      return 'secondary';
    case 'published':
      return 'default';
    default:
      return 'outline';
  }
};

export const formatStatus = (status: string) => {
  switch (status) {
    case 'Review Needed':
      return 'Review';
    case 'published':
      return 'Published';
    case 'draft':
      return 'Draft';
    default:
      return status;
  }
}; 