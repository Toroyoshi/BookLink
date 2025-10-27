class Loan:
    def _init_(self, loan_id, user_id, product_details_id):
        self.loan_id = loan_id
        self.user_id = user_id
        self.product_id = product_details_id

    def to_dict(self):
        return {
            'loan_id': self.loan_id, #emprestimos_reservas
            'user_id': self.user_id, #utilizadores
            'product_details': self.product_id #catálogo
        }