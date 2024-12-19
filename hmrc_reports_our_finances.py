from cls_helper_sql import SQL_Helper
from tables import *


class HMRC_People(People):
    def __init__(self, code):
        super().__init__(code)

        self.hmrc_person_details = HMRC_PeopleDetails(code)

    def get_bank_account_number(self):
        refunds_to = self.hmrc_person_details.get_refunds_to()
        return BankAccounts(refunds_to).get_account_number()

    def get_bank_name(self):
        refunds_to = self.hmrc_person_details.get_refunds_to()
        return BankAccounts(refunds_to).get_bank_name()

    def get_branch_sort_code(self):
        refunds_to = self.hmrc_person_details.get_refunds_to()
        return BankAccounts(refunds_to).get_sort_code()

    def get_national_insurance_number(self):
        return self.hmrc_person_details.get_national_insurance_number()

    def get_refunds_to(self):
        return self.hmrc_person_details.get_refunds_to()

    def get_spouse_code(self):
        return self.hmrc_person_details.get_spouse_code()

    def get_uk_marriage_date(self):
        return self.hmrc_person_details.get_uk_marriage_date()

    def get_unique_tax_reference(self) -> str:
        return self.hmrc_person_details.get_unique_tax_reference()

    def get_utr_check_digit(self) -> str:
        return self.hmrc_person_details.get_utr_check_digit()


class HMRC:
    def __init__(self, person_code, tax_year):
        self.person_code = person_code
        self.tax_year = tax_year

        self.person = HMRC_People(person_code)

        spouse_code = self.person.get_spouse_code()

        self.spouse = HMRC_People(spouse_code)

        self.categories = Categories()
        self.transactions = Transactions()

        self.sql = SQL_Helper().select_sql_helper("SQLite")

        # self.list_categories()

    def append_section(self, answers, section):
        section = f"\n{section.upper()}"
        this_return = f"{self.person.get_name()} {self.tax_year}\n"

        answers.append([section, "", "", this_return])

        answers.append(["Page", "Box", "Question", "Answer"])

        return answers

    def call_method(self, method_name):
        try:
            method = getattr(self, method_name)
            return method()
        except AttributeError:
            print(f"Method {method_name} not found")

    def format_answer(self, string_list) -> str:
        if len(string_list[2]) > 0:
            widths = [8, 5, 55]  # Define column widths

            # Use zip to pair strings with widths and format them in one step
            formatted_parts = [
                f"{string:<{width}}" for string, width in zip(string_list[:3], widths)
            ]
        else:
            widths = [69]  # Define column widths

            # Use zip to pair strings with widths and format them in one step
            formatted_parts = [
                f"{string:<{width}}" for string, width in zip(string_list[:1], widths)
            ]

        # Join the formatted parts and append the fourth string without formatting
        return "".join(formatted_parts) + string_list[3]

    def get_total_tax_due(self):
        return "Not applicable"

    def get_total_tax_overpaid(self):
        return "Not applicable"

    def get_student_loan_repayment_due(self):
        return "Not applicable"

    def get_postgraduate_loan_repayment_due(self):
        return "Not applicable"

    def get_class_4_nics_due(self):
        return "Not applicable"

    def get_class_2_nics_due(self):
        return "Not applicable"

    def get_capital_gains_tax_due(self):
        return "Not applicable"

    def get_pension_charges_due(self):
        return "Not applicable"

    def get_underpaid_tax_for_earlier_years(self):
        return "Not applicable"

    def get_underpaid_tax(self):
        return "Not applicable"

    def get_outstanding_debt_in_tax_code(self):
        return "Not applicable"

    def get_reduce_next_year_payments_on_account__yes_no_(self):
        return "Not applicable"

    def get_first_payment_on_account_for_next_year(self):
        return "Not applicable"

    def get_blind_person_s_surplus_allowance_you_can_have(self):
        return "Not applicable"

    def get_married_people_s_surplus_allowance_you_can_have(self):
        return "Not applicable"

    def get_increase_in_tax_due_to_adjustments_to_an_earlier_year(self):
        return "Not applicable"

    def get_decrease_in_tax_due_to_adjustments_to_an_earlier_year(self):
        return "Not applicable"

    def get_any_repayments_claimed_for_next_year(self):
        return "Not applicable"

    def get_please_give_any_other_information_in_this_space(self):
        return "Not applicable"

    def get_additional_information__yes_no_(self):
        return "Maybe: Married couples allowance section"
        # return False

    def get_number_of_properties_rented_out(self):
        return "Not applicable"

    def get_ceased_renting__consider_cgt__yes_no_(self):
        return "Not applicable"

    def get_property_let_jointly__yes_no_(self):
        return "Not applicable"

    def get_rent_a_room_relief__yes_no_(self):
        return "Not applicable"

    def get_total_rents_and_other_income_from_property(self):
        return "Not applicable"

    def get_property_income_allowance(self):
        return "Not applicable"

    def get_ukp_cash_basis__yes_no_(self):
        return "Not applicable"

    def get_tax_taken_off_any_income_in_box_20(self):
        return "Not applicable"

    def get_premiums_for_the_grant_of_a_lease(self):
        return "Not applicable"

    def get_reverse_premiums(self):
        return "Not applicable"

    def get_rent__rates__insurance_and_ground_rents(self):
        return "Not applicable"

    def get_property_repairs_and_maintenance(self):
        return "Not applicable"

    def get_non_residential_finance_property_costs(self):
        return "Not applicable"

    def get_legal__management_and_other_professional_fees(self):
        return "Not applicable"

    def get_costs_of_services_provided__including_wages(self):
        return "Not applicable"

    def get_other_allowable_property_expenses(self):
        return "Not applicable"

    def get_private_use_adjustment(self):
        return "Not applicable"

    def get_balancing_charges(self):
        return "Not applicable"

    def get_structures_and_buildings_allowance(self):
        return "Not applicable"

    def get_electric_charge_point_allowance(self):
        return "Not applicable"

    def get_freeport_allowance(self):
        return "Not applicable"

    def get_zero_emissions_allowance(self):
        return "Not applicable"

    def get_all_other_capital_allowances(self):
        return "Not applicable"

    def get_costs_of_replacing_domestic_items(self):
        return "Not applicable"

    def get_rent_a_room_exempt_amount(self):
        return "Not applicable"

    def get_adjusted_profit_for_the_year(self):
        return "Not applicable"

    def get_taxable_profit_for_the_year(self):
        return "Not applicable"

    def get_adjusted_loss_for_the_year(self):
        return "Not applicable"

    def get_loss_set_off_against_income(self):
        return "Not applicable"

    def get_loss_to_carry_forward(self):
        return "Not applicable"

    def get_residential_property_finance_costs(self):
        return "Not applicable"

    def get_unused_residential_finance_costs_brought_forward(self):
        return "Not applicable"

    def get_answers(self):
        answers = []
        for question, page, section, box, method_name in self.get_questions():
            if box == "1":
                answers = self.append_section(answers, section)

            answer = self.call_method(method_name)

            answers.append([page, box, question, answer])
            # match question:
            #     case "Declaration":
            #         answer = "Sign & date"
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Collect by PAYE":
            #         answer = "NO"
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Collect small amounts by PAYE":
            #         answer = "NO"
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Date of marriage":
            #         answer = "10/04/2018"
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your spouse's first name":
            #         answer = self.spouse.get_first_name()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your spouse's last name":
            #         answer = self.spouse.get_last_name()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your date of birth":
            #         answer = self.person.get_date_of_birth()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your spouse's date of birth":
            #         answer = self.spouse.get_date_of_birth()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your phone number":
            #         answer = self.person.get_phone_number()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your National Insurance number":
            #         answer = self.person.get_national_insurance_number()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Your spouse's National Insurance number":
            #         answer = self.spouse.get_national_insurance_number()
            #         answers[question] = f"{page} {box} {question}: {answer}"
            #     case "Total":
            #         category = self.categories.fetch_by_page_box(
            #             page, box, self.person_code
            #         )
            #         if category:
            #             hmrc_category = HMRC_Category(category, self.person_code)
            #             question = hmrc_category.get_description()

            #             amount = self.transactions.fetch_total_by_tax_year_category(
            #                 self.tax_year, category
            #             )

            #             answers[question] = (
            #                 f"{page} {box} {question}: £{amount:,.2f}"
            #             )
            #         else:
            #             sys.stderr.write(
            #                 f'{page}, {box}, {self.person_code}, "Category not found"\n'
            #             )
            #     case _:
            #         sys.stderr.write(f"Unhandled question: {question}\n")

        return answers

    def get_any_tax_taken_off_box_17(self):
        return 0

    def get_benefit_from_pre_owned_assets(self):
        return 0

    def get_capital_gains_tax_summary__yes_no_(self):
        return False

    def get_computations_provided__yes_no_(self):
        return False

    def get_description_of_income_in_boxes_17_and_20(self):
        return ""

    def get_dividends_from_uk_companies(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Dividends from UK companies"
        )

    def get_foreign_dividends(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Foreign dividends"
        )

    def get_foreign__yes_no_(self):
        return False

    def get_full_utr(self) -> str:
        utr: str = self.person.get_unique_tax_reference()
        utr_check_digit: str = self.person.get_utr_check_digit()
        return utr + utr_check_digit

    def get_how_many_businesses(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} SES%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_how_many_employments(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} EMP%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_lump_sum_pension___available_lifetime_allowance(self):
        return "Not applicable"

    def get_non_lump_sum_pension___available_lifetime_allowance(self):
        return "Not applicable"

    def get_lifetime_allowance_tax_paid_by_your_pension_scheme(self):
        return "Not applicable"

    def get_amount_saved_to_pension___available_lifetime_allowance(self):
        return "Not applicable"

    def get_annual_allowance_tax_paid(self):
        return "Not applicable"

    def get_amount_subject_to_overseas_transfer_charge(self):
        return "Not applicable"

    def get_tax_paid_on_overseas_transfer_charge(self):
        return "Not applicable"

    def get_pension_scheme_tax_reference_number(self):
        return "Not applicable"

    def get_unauthorised_pension_payment_not_surcharged_(self):
        return "Not applicable"

    def get_unauthorised_pension_payment_surcharged_(self):
        return "Not applicable"

    def get_foreign_tax_paid_on_an_unauthorised_payment(self):
        return "Not applicable"

    def get_taxable_short_service_refund__overseas_only_(self):
        return "Not applicable"

    def get_box_17_is_not_in_use(self):
        return "Not applicable"

    def get_foreign_tax_paid_on_box_16(self):
        return "Not applicable"

    def get_tax_avoidance_scheme_reference_number(self):
        return "Not applicable"

    def get_tax_year_expected_advantage_arises(self):
        return "Not applicable"

    def get_description_of_business(self):
        return "Not applicable"

    def get_postcode_of_your_business_address(self):
        return "Not applicable"

    def get_have_business_details_changed__yes_no_(self):
        return "Not applicable"

    def get_are_you_a_foster_carer(self):
        return "Not applicable"

    def get_business_start_date__in_this_tax_year_(self):
        return "Not applicable"

    def get_business_end_date__in_this_tax_year_(self):
        return "Not applicable"

    def get_date_the_books_are_made_up_to(self):
        return "Not applicable"

    def get_cash_basis__yes_no_(self):
        return "Not applicable"

    def get_turnover(self):
        return "Not applicable"

    def get_any_other_business_income_not_included_in_box_9(self):
        return "Not applicable"

    def get_trading_income_allowance(self):
        return "Not applicable"

    def get_turnover_was_below__85k__total_expenses_in_box_20(self):
        return "See box 20"

    def get_total_allowable_expenses(self):
        return "Not applicable"

    def get_net_profit(self):
        return "Not applicable"

    def get_net_loss(self):
        return "Not applicable"

    def get_annual_investment_allowance(self):
        return "Not applicable"

    def get_allowance_for_small_balance_of_unrelieved_expenditure(self):
        return "Not applicable"

    def get_zero_emission_car_allowance(self):
        return "Not applicable"

    def get_other_capital_allowances(self):
        return "Not applicable"

    def get_the_structures_and_buildings_allowance(self):
        return "Not applicable"

    def get_freeport___investment_zones_allowance(self):
        return "Not applicable"

    def get_total_balancing_charges(self):
        return "Not applicable"

    def get_goods_services_for_your_own_use(self):
        return "Not applicable"

    def get_net_business_profit_for_tax_purposes(self):
        return "Not applicable"

    def get_loss_brought_forward(self):
        return "Not applicable"

    def get_other_business_income_not_included_in_boxes_9_or_10(self):
        return "Not applicable"

    def get_total_taxable_profits_from_this_business(self):
        return "Not applicable"

    def get_net_business_loss_for_tax_purposes(self):
        return "Not applicable"

    def get_loss_from_this_tax_year_set_off_against_other_income(self):
        return "Not applicable"

    def get_loss_to_be_carried_back_to_previous_years(self):
        return "Not applicable"

    def get_total_loss_to_carry_forward(self):
        return "Not applicable"

    def get_total_profits____6_725_voluntary_class_2_nics__yes_no_(self):
        return "Not applicable"

    def get_are_you_exempt_from_paying_class_4_nics(self):
        return "Not applicable"

    def get_total_construction_industry_scheme__cis__deductions(self):
        return "Not applicable"

    def get_how_many_partnerships(self):
        return 0

    def get_jobseeker_s_allowance(self):
        return 0

    def get_more_pages__yes_no_(self):
        return False

    def get_other_dividends(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Other dividends"
        )

    def get_other_taxable_income(self):
        return 0

    def get_payments_to_pension_schemes__relief_at_source_(self):
        my_payments = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, "HMRC S pension contribution"
        )
        hmrc_contribution = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, "HMRC S pension tax relief"
        )
        return my_payments + hmrc_contribution

    def get_pensions__other_than_state_pension_(self):
        return 0

    def get_residence__remittance_basis_etc__yes_no_(self):
        return False

    def get_questions(self):
        return HMRC_QuestionsByYear(self.tax_year).get_questions()

    def get_spouse_code(self):
        return self.person.get_spouse_code()

    def get_state_pension(self):
        return 0

    def get_state_pension_lump_sum(self):
        return 0

    def get_tax_taken_off_box_9(self):
        return 0

    def get_tax_taken_off_box_11(self):
        return 0

    def get_tax_taken_off_foreign_dividends(self):
        return 0

    def get_tax_taken_off_incapacity_benefit_in_box_13(self):
        return 0

    def get_taxable_incapacity_benefit(self):
        return 0

    def get_taxed_uk_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Taxed UK interest"
        )

    def get_payments_to_annuity_tax_relief_not_claimed(self):
        return "Not applicable"

    def get_payments_to_employers_scheme_where_no_tax_deducted(self):
        return "Not applicable"

    def get_payments_to_overseas_pension_scheme(self):
        return "Not applicable"

    def get_gift_aid_payments(self):
        return "Not applicable"

    def get_total_of_any__one_off__payments_in_box_5(self):
        return "Not applicable"

    def get_gift_aid_payments_from_previous_tax_year_(self):
        return "Not applicable"

    def get_gift_aid_payments_after_end_of_tax_year(self):
        return "Not applicable"

    def get_value_of_shares_dividends_gifted_to_charities(self):
        return "Not applicable"

    def get_value_of_land_or_buildings_gifted_to_charities(self):
        return "Not applicable"

    def get_value_gifted_to_non_uk_charities_in_box_9_and_10(self):
        return "Not applicable"

    def get_for_how_many_children__cb_(self):
        return "Not applicable"

    def get_date_cb_stopped(self):
        return "Not applicable"

    def get_your_spouse_s_first_name(self):
        return self.spouse.get_first_name()

    def get_your_spouse_s_last_name(self):
        return self.spouse.get_last_name()

    def get_your_spouse_s_national_insurance_number(self):
        return self.spouse.get_national_insurance_number()

    def get_your_spouse_s_date_of_birth(self):
        return self.spouse.get_uk_date_of_birth()

    def get_marriage_date(self):
        return self.spouse.get_uk_marriage_date()

    def get_refunded_or_off_set_income_tax(self):
        return "Not applicable"

    def get_use_paye_for_small_amount_payments__yes_no_(self):
        return "No"

    def get_use_paye_for_tax_on_savings__yes_no_(self):
        return "No"

    def get_bank_name(self):
        return self.person.get_bank_name()

    def get_bank_account_holder(self):
        return self.person.get_name()

    def get_branch_sort_code(self):
        return self.person.get_branch_sort_code()

    def get_bank_account_number(self):
        return self.person.get_bank_account_number()

    def get_building_society_reference_number(self):
        return "Not applicable"

    def get_cheque__yes_no_(self):
        return "No"

    def get_did_you_put_a_nominee_s_name_in_box_5__yes_no_(self):
        return "No"

    def get_is_your_nominee_your_tax_advisor__yes_no_(self):
        return "Not applicable"

    def get_nominee_s_address(self):
        return "Not applicable"

    def get_nominee_s_postcode(self):
        return "Not applicable"

    def get_signature_to_authorise_nominee(self):
        return "Not applicable"

    def get_tax_advisor_s_name(self):
        return "Not applicable"

    def get_tax_advisor_s_phone_number(self):
        return "Not applicable"

    def get_tax_advisor_s_address_and_postcode(self):
        return "Not applicable"

    def get_tax_advisor_s_reference(self):
        return "Not applicable"

    def get_any_other_information(self):
        return "Not applicable"

    def get_provisional_figures__yes_no_(self):
        return "Not applicable"

    def get_supplementary_pages_enclodsed__yes_no_(self):
        return "Not applicable"

    def get_declaration_signature(self):
        return "Not applicable"

    def get_declaration_date(self):
        return "Not applicable"

    def get_signing_capacity_if_signing_for_someone_else(self):
        return "Not applicable"

    def get_name_of_the_peson_you_ve_signed_for(self):
        return "Not applicable"

    def get_if_you_filled_in_boxes_23_and_24_enter_your_name(self):
        return "Not applicable"

    def get_and_your_address(self):
        return "Not applicable"

    def get_gilt_interest_after_tax_taken_off(self):
        return "Not applicable"

    def get_tax_taken_off(self):
        return "Not applicable"

    def get_gross_amount_before_tax(self):
        return "Not applicable"

    def get_uk_gains_where_tax_was_treated_as_paid(self):
        return "Not applicable"

    def get_number_of_years_policy_was_last_held_or_received_gain(self):
        return "Not applicable"

    def get_uk_gains_where_tax_was_not_treated_as_paid(self):
        return "Not applicable"

    def get_how_many_years_policy_was_last_held_or_received_gain(self):
        return "Not applicable"

    def get_gains_from_voided_isas(self):
        return "Not applicable"

    def get_years_voided_isas_held(self):
        return "Not applicable"

    def get_tax_taken_off_gain_in_box_8(self):
        return "Not applicable"

    def get_deficiency_relief(self):
        return "Not applicable"

    def get_stock_dividends(self):
        return "Not applicable"

    def get_bonus_issues(self):
        return "Not applicable"

    def get_loans_written_off(self):
        return "Not applicable"

    def get_post_cessation_receipts_amount(self):
        return "Not applicable"

    def get_earlier_year_tax_year_to_be_taxed(self):
        return "Not applicable"

    def get_share_schemes_taxable_amount(self):
        return "Not applicable"

    def get_box_2_is_not_is_use(self):
        return "Not applicable"

    def get_taxable_lump_sums(self):
        return "Not applicable"

    def get_lump_sums_employer_financed_retirement_benefits_scheme(self):
        return "Not applicable"

    def get_redundancy_payments(self):
        return "Not applicable"

    def get_tax_taken_off_boxes_3_to_5(self):
        return "Not applicable"

    def get_is_box_6_blank_as_tax_inc__in_box_2_of__employment_(self):
        return "Not applicable"

    def get_exemptions_for_amounts_entered_in_box_4(self):
        return "Not applicable"

    def get_compensation_and_lump_sums_up_to__30_000_exemption(self):
        return "Not applicable"

    def get_disability_and_foreign_service_deduction(self):
        return "Not applicable"

    def get_seafarers__earnings_deduction(self):
        return "Not applicable"

    def get_foreign_earnings_not_taxable_in_the_uk(self):
        return "Not applicable"

    def get_foreign_tax_where_tax_credit_not_claimed(self):
        return "Not applicable"

    def get_exempt_overseas_employee_contributions(self):
        return "Not applicable"

    def get_uk_patent_royalty_payments_made(self):
        return "Not applicable"

    def get_subscriptions_for_venture_capital_trust_shares(self):
        return "Not applicable"

    def get_subscriptions_for_enterprise_investment_scheme_shares(self):
        return "Not applicable"

    def get_community_investment_tax_relief(self):
        return "Not applicable"

    def get_annual_payments_made(self):
        return "Not applicable"

    def get_qualifying_loan_interest_payable_in_the_year(self):
        return "Not applicable"

    def get_post_cessation_trade_relief_and_certain_other_losses(self):
        return "Not applicable"

    def get_pre_incorporation_losses(self):
        return "Not applicable"

    def get_maintenance_payments(self):
        return "Not applicable"

    def get_payments_to_a_trade_union_for_death_benefits(self):
        return "Not applicable"

    def get_relief_claimed_on_a_qualifying_distribution(self):
        return "Not applicable"

    def get_shares_under_the_seed_enterprise_investment_scheme(self):
        return "Not applicable"

    def get_box_11_is_not_in_use(self):
        return "Not applicable"

    def get_non_deductible_loan_interest_letting_pship_investments(self):
        return "Not applicable"

    def get_not_applicable(self):
        return "Not applicable"

    def get_earlier_years__losses(self):
        return "Not applicable"

    def get_total_unused_losses_carried_forward(self):
        return "Not applicable"

    def get_relief_now_for_following_year_trade_losses(self):
        return "Not applicable"

    def get_amount_in_box_3_not_subject_to_income_tax_relief_limit(self):
        return "Not applicable"

    def get_tax_year_for_which_you_re_claiming_relief_in_box_3_(self):
        return "Not applicable"

    def get_amount_of_payroll_giving(self):
        return "Not applicable"

    def get_gift_aid_payments_to_non_uk_charities_in_box_6(self):
        return "Not applicable"

    def get_registered_blind_(self):
        return False

    def get_local_authority_or_other_register(self):
        return "Not applicable"

    def get_do_you_want_spouse_s_surplus_allowance(self):
        return "Not applicable"

    def get_should_your_spouse_get_your_surplus_allowance(self):
        return "Not applicable"

    def get_have_you_received_student_loans_company_notification(self):
        return False

    def get_any_employer_deducted_student_loan(self):
        return "Not applicable"

    def get_any_employer_deducted_post_grad_loan(self):
        return "Not applicable"

    def get_how_much_child_benefit__cb__received(self):
        return 0.0

    def get_title(self):
        full_utr = self.get_full_utr()
        person_name = self.person.get_name()
        tax_year = self.tax_year

        return f"HMRC {tax_year} tax return for {person_name} - UTR {full_utr}\n"

    def get_total_amount_of_allowable_expenses(self):
        return 0

    def get_total_of_any__one_off__payments_in_box_1(self):
        my_payments = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, "HMRC S pension contribution"
        )
        hmrc_contribution = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, "HMRC S pension tax relief"
        )
        return my_payments + hmrc_contribution

    def get_total_of_any_other_taxable_state_pensions_and_benefits(self):
        return 0

    def get_trusts_etc__yes_no_(self):
        return False

    def get_untaxed_foreign_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Untaxed foreign interest"
        )

    def get_untaxed_uk_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Untaxed UK interest"
        )

    def get_uk_property__yes_no_(self):
        # search the transactions table for any records in this tax year
        # which have a UKP income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} UKP income%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def get_year_category_total(self, tax_year, category):
        return self.transactions.fetch_total_by_tax_year_category(tax_year, category)

    def get_your_date_of_birth(self):
        return self.person.get_uk_date_of_birth()

    def get_your_name_and_address(self):
        return "Leave blank - not changed"

    def get_your_national_insurance_number(self):
        return self.person.get_national_insurance_number()

    def get_your_phone_number(self):
        return self.person.get_phone_number()

    def get_were_you_employed_in_this_tax_year(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(*)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} EMP%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def get_were_you_in_partnership_s__this_tax_year(self):
        return False

    def get_were_you_self_employed_in_this_tax_year(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(*)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} SES%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def list_categories(self):
        query = (
            self.transactions.query_builder()
            .select_raw("DISTINCT Category")
            .where(
                f'"Tax year" = "{self.tax_year}" AND "Category" LIKE "HMRC {self.person_code}%" ORDER BY Category'
            )
            .build()
        )

        categories = self.sql.fetch_all(query)
        for row in categories:
            print(row[0])

    def print_answer(self, page, box, question, answer):
        if isinstance(answer, bool):
            answer = "Yes" if answer else "No"
        elif isinstance(answer, float):
            answer = f"£{answer:,.2f}"
        elif isinstance(answer, int):
            answer = f"{answer:,}"
        elif isinstance(answer, str):
            pass  # No change needed for strings
        else:
            answer = str(answer)

        formatted_answer = self.format_answer([page, box, question, answer])

        print(formatted_answer)

    def print_report(self):
        print(self.get_title())

        answers = self.get_answers()

        for page, box, question, answer in answers:
            self.print_answer(page, box, question, answer)

        print(
            "\n=========================================================================================\n"
        )

    def print_hmrc_report(self):
        tax_year = self.tax_year
        person_code = self.person_code

        print("\nPage TR 3\n")

        question_number = 1
        question = "Taxed UK interest: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Untaxed UK interest: "
        answer = f"{question_number} {question}"

        amount = self.get_year_category_total(
            tax_year, f"HMRC {person_code} Untaxed UK interest"
        )

        if amount:
            answer += f"£{amount:,.2f}"

        print(answer)

        question_number += 1
        question = "Untaxed foreign interest: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Dividends from UK companies: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Other dividends: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Foreign dividends: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off foreign dividends: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "State pension: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "State pension lump sum: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off box 9: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Other pensions: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off box 11: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Taxable incapacity benefit: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off box 13: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Jobseeker's Allowance: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any other taxable State Pensions and benefits: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Other taxable income: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total amount of allowable expenses: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Any tax taken off box 17: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Benefit from pre-owned assets: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Description of income in boxes 17 and 20: "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TR 4\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)
        print(answer)

        print("\nPage TR 5\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number = 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number = 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TR 6\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)
        print(answer)

        print("\nPage TR 7\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TR 8\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 3\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 4\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage SES 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage SES 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage UKP 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage UKP 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TC 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TC 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        query = f"""
            SELECT Category, SUM(Nett) 
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category LIKE 'HMRC {person_code}%'
            GROUP BY Category
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def main():
    hmrc = HMRC("B", "2023 to 2024")
    hmrc.print_report()

    hmrc = HMRC("S", "2023 to 2024")
    hmrc.print_report()


if __name__ == "__main__":
    main()
